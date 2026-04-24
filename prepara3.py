from pyspark.sql import SparkSession

# Inicializar sesión de Spark
spark = (
    SparkSession.builder.appName("CargarDatosPostgres")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.5.4")
    .getOrCreate()
)

# Configuración de la conexión a la base de datos
url = "jdbc:postgresql://localhost:5432/postgres"
user = "root"
password = "sdbz.jvj1"

# Propiedades JDBC que se pasarán a los métodos de escritura de PySpark
jdbc_properties = {
    "user": user,
    "password": password,
    "driver": "org.postgresql.Driver",
}

try:
    print("1. Cargando education.csv en la tabla tarea3.education...")
    df_education = spark.read.csv("education.csv", header=True, inferSchema=True)
    df_education.write.jdbc(
        url=url, table="tarea3.education", mode="append", properties=jdbc_properties
    )
    print("Datos de education cargados exitosamente.")

    print("2. Cargando jobs.csv en la tabla tarea3.jobs...")
    df_jobs = spark.read.csv("jobs.csv", header=True, inferSchema=True)
    df_jobs.write.jdbc(
        url=url, table="tarea3.jobs", mode="append", properties=jdbc_properties
    )
    print("Datos de jobs cargados exitosamente.")

    print("3. Cargando bank-full.csv en la tabla tarea3.bank_sample...")
    # Leer el archivo delimitado por punto y coma
    df_bank = spark.read.csv("bank-full.csv", sep=";", header=True, inferSchema=True)

    # Renombrar columnas 'job' y 'education' a 'job_id' y 'education_id'
    # para que coincidan con la estructura (las Foreign Keys) de la tabla en base de datos.
    # El resto de columnas (age, marital, balance, etc.) ya coinciden por nombre.
    df_bank = df_bank.withColumnRenamed("job", "job_id").withColumnRenamed(
        "education", "education_id"
    )

    df_bank.write.jdbc(
        url=url, table="tarea3.bank", mode="append", properties=jdbc_properties
    )
    print("Datos de bank-full.csv cargados exitosamente.")

except Exception as e:
    print(f"Ocurrió un error durante la carga de datos: {e}")

finally:
    # Finalizar la sesión de Spark
    spark.stop()
