from pyspark.sql import SparkSession

# 1. Inicializar sesión de Spark
spark = (
    SparkSession.builder.appName("ConsultaBanco")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.5.4")
    .getOrCreate()
)

# 2. Configuración de la conexión a la base de datos
url = "jdbc:postgresql://localhost:5432/postgres"
user = "root"
password = "sdbz.jvj1"

jdbc_properties = {
    "user": user,
    "password": password,
    "driver": "org.postgresql.Driver",
}

try:
    # 3. Realizar la consulta cargando las tablas como DataFrames
    df_bank = spark.read.jdbc(url=url, table="tarea3.bank", properties=jdbc_properties)
    df_jobs = spark.read.jdbc(url=url, table="tarea3.jobs", properties=jdbc_properties)
    df_education = spark.read.jdbc(
        url=url, table="tarea3.education", properties=jdbc_properties
    )

    # Hacer el JOIN con la tabla de jobs para sustituir el código por la descripción
    df_bank_jobs = (
        df_bank.join(df_jobs, df_bank.job_id == df_jobs.codigo, "left")
        .drop("job_id", "codigo")
        .withColumnRenamed("descripcion", "job")
    )

    # Hacer el JOIN con la tabla de education para sustituir el código por la descripción
    df_final = (
        df_bank_jobs.join(
            df_education, df_bank_jobs.education_id == df_education.codigo, "left"
        )
        .drop("education_id", "codigo")
        .withColumnRenamed("descripcion", "education")
    )

    # Reorganizar las columnas para que coincidan con el formato original (opcional pero recomendado)
    columnas_ordenadas = [
        "age",
        "job",
        "marital",
        "education",
        "default",
        "balance",
        "housing",
        "loan",
        "contact",
        "day",
        "month",
        "duration",
        "campaign",
        "pdays",
        "previous",
        "poutcome",
        "y",
    ]

    # Filtrar solo las columnas que existan en el DataFrame resultante
    columnas_finales = [col for col in columnas_ordenadas if col in df_final.columns]
    if columnas_finales:
        df_final = df_final.select(*columnas_finales)

    # 4. Desplegar las primeras 10 líneas del resultado
    print("----- Primeras 10 líneas del resultado -----")
    df_final.show(10, truncate=False)

    # ======================================================
    # 3. Cantidad de valores nulos en df_final
    # ======================================================
    from pyspark.sql.functions import col, sum as _sum
    
    print("\n----- Cantidad de valores nulos por columna -----")
    # Se suma 1 por cada valor nulo encontrado en cada columna
    exprs = [_sum(col(c).isNull().cast("int")).alias(c) for c in df_final.columns]
    df_nulls = df_final.select(*exprs)
    df_nulls.show()

    # ======================================================
    # 4. Identificar variables categóricas y numéricas
    # ======================================================
    from pyspark.sql.types import StringType
    
    # En PySpark, las variables de tipo StringType son típicamente las categóricas
    categorical_cols = [f.name for f in df_final.schema.fields if isinstance(f.dataType, StringType)]
    numerical_cols = [f.name for f in df_final.schema.fields if not isinstance(f.dataType, StringType)]
    
    print("----- Tipos de Variables Identificadas -----")
    print(f"Variables Categóricas ({len(categorical_cols)}): {categorical_cols}")
    print(f"Variables Numéricas ({len(numerical_cols)}): {numerical_cols}")
    
    # "Definirlas así": Las variables en PySpark ya tienen su tipo definido en el schema.
    # Si se requiriera indexarlas para un modelo de Machine Learning, 
    # se utilizaría StringIndexer de pyspark.ml.feature.

    # ======================================================
    # 5. Generar los gráficos de distribución de cada variable
    # ======================================================
    print("\nGenerando gráficos de distribución...")
    # PySpark delega la graficación a librerías de Python estándar (pandas y matplotlib/seaborn)
    # Convertimos el DataFrame a Pandas (banco-full tiene ~45k filas, lo cual cabe en memoria local)
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    pdf = df_final.toPandas()
    sns.set(style="whitegrid")
    
    # 5.1 Distribución de variables Numéricas
    # Creamos una figura con subplots para las numéricas
    num_cols_count = len(numerical_cols)
    fig, axes = plt.subplots(nrows=(num_cols_count + 2) // 3, ncols=3, figsize=(15, 12))
    axes = axes.flatten()
    
    for i, col_name in enumerate(numerical_cols):
        sns.histplot(pdf[col_name], kde=True, ax=axes[i], bins=30, color="skyblue")
        axes[i].set_title(f'Distribución de {col_name}')
        axes[i].set_xlabel(col_name)
        axes[i].set_ylabel('Frecuencia')
        
    # Ocultar subplots vacíos
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
        
    plt.tight_layout()
    plt.show()

    # 5.2 Distribución de variables Categóricas
    # Creamos otra figura con subplots para las categóricas
    cat_cols_count = len(categorical_cols)
    fig, axes = plt.subplots(nrows=(cat_cols_count + 2) // 3, ncols=3, figsize=(18, 18))
    axes = axes.flatten()
    
    for i, col_name in enumerate(categorical_cols):
        sns.countplot(data=pdf, x=col_name, ax=axes[i], order=pdf[col_name].value_counts().index, palette="viridis")
        axes[i].set_title(f'Distribución de {col_name}')
        axes[i].set_xlabel(col_name)
        axes[i].set_ylabel('Cantidad')
        axes[i].tick_params(axis='x', rotation=45)
        
    # Ocultar subplots vacíos
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
        
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Ocurrió un error al ejecutar la consulta: {e}")
    
finally:
    # Finalizar la sesión de Spark
    spark.stop()
