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
    df_education = spark.read.jdbc(url=url, table="tarea3.education", properties=jdbc_properties)

    # Hacer el JOIN con la tabla de jobs para sustituir el código por la descripción
    df_bank_jobs = df_bank.join(
        df_jobs, 
        df_bank.job_id == df_jobs.codigo, 
        "left"
    ).drop("job_id", "codigo").withColumnRenamed("descripcion", "job")

    # Hacer el JOIN con la tabla de education para sustituir el código por la descripción
    df_final = df_bank_jobs.join(
        df_education, 
        df_bank_jobs.education_id == df_education.codigo, 
        "left"
    ).drop("education_id", "codigo").withColumnRenamed("descripcion", "education")

    # Reorganizar las columnas para que coincidan con el formato original (opcional pero recomendado)
    columnas_ordenadas = [
        "age", "job", "marital", "education", "default", "balance", 
        "housing", "loan", "contact", "day", "month", "duration", 
        "campaign", "pdays", "previous", "poutcome", "y"
    ]
    
    # Filtrar solo las columnas que existan en el DataFrame resultante
    columnas_finales = [col for col in columnas_ordenadas if col in df_final.columns]
    if columnas_finales:
        df_final = df_final.select(*columnas_finales)

    # 4. Desplegar las primeras 10 líneas del resultado
    print("----- Primeras 10 líneas del resultado -----")
    df_final.show(10, truncate=False)

except Exception as e:
    print(f"Ocurrió un error al ejecutar la consulta: {e}")

finally:
    # Finalizar la sesión de Spark
    spark.stop()
