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
    # Calcularemos las distribuciones de forma distribuida utilizando únicamente PySpark.
    # Una vez agregados los datos (conteos o bins), utilizamos matplotlib para visualizarlos,
    # evitando traer todo el dataset a la memoria local con toPandas().
    import matplotlib.pyplot as plt
    
    # 5.1 Distribución de variables Numéricas de forma separada
    variables_solicitadas = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    
    print(f"Generando gráficos individuales calculados con PySpark para: {variables_solicitadas}")
    for col_name in variables_solicitadas:
        if col_name in df_final.columns:
            # Calcular el histograma directamente en PySpark (100% distribuido)
            # RDD histogram devuelve los bordes de los bins y los conteos
            bins, counts = df_final.select(col_name).rdd.flatMap(lambda x: x).histogram(30)
            
            # Graficar usando solo los datos agregados
            plt.figure(figsize=(8, 5))
            widths = [bins[i+1] - bins[i] for i in range(len(counts))]
            centers = [bins[i] + widths[i]/2 for i in range(len(counts))]
            
            plt.bar(centers, counts, width=widths, color="skyblue", edgecolor="black")
            plt.title(f'Distribución de {col_name} (Procesado en PySpark)')
            plt.xlabel(col_name)
            plt.ylabel('Frecuencia')
            plt.tight_layout()
            plt.show()
            
    # 5.2 Distribución de variables Categóricas de forma separada
    for col_name in categorical_cols:
        # Calcular el conteo de categorías directamente en PySpark
        counts_rows = df_final.groupBy(col_name).count().orderBy("count", ascending=False).collect()
        
        # Extraer las etiquetas y valores ya agregados
        labels = [str(row[col_name]) for row in counts_rows]
        values = [row["count"] for row in counts_rows]
        
        plt.figure(figsize=(8, 5))
        plt.bar(labels, values, color="mediumseagreen", edgecolor="black")
        plt.title(f'Distribución de {col_name} (Procesado en PySpark)')
        plt.xlabel(col_name)
        plt.ylabel('Cantidad')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

except Exception as e:
    print(f"Ocurrió un error al ejecutar la consulta: {e}")
    
finally:
    # Finalizar la sesión de Spark
    spark.stop()
