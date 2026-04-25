from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, when

# 1. Inicializar sesión de Spark
spark = (
    SparkSession.builder.appName("AnalisisUnknowns")
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

    # 4. Hacer los JOIN para tener el set de datos completo con descripciones
    df_bank_jobs = (
        df_bank.join(df_jobs, df_bank.job_id == df_jobs.codigo, "left")
        .drop("job_id", "codigo")
        .withColumnRenamed("descripcion", "job")
    )
    df_final = (
        df_bank_jobs.join(df_education, df_bank_jobs.education_id == df_education.codigo, "left")
        .drop("education_id", "codigo")
        .withColumnRenamed("descripcion", "education")
    )

    # 5. Identificar variables con valores "unknown"
    print("Analizando el set de datos en búsqueda de valores 'unknown'...")
    
    # Creamos una lista de expresiones. Para cada columna, verificamos si su valor 
    # (convertido a texto) es exactamente "unknown", sumando 1 por cada coincidencia.
    exprs = [
        _sum(when(col(c).cast("string").rlike("(?i)^unknown$"), 1).otherwise(0)).alias(c) 
        for c in df_final.columns
    ]
    
    df_unknowns = df_final.select(*exprs)
    
    print("\n----- Conteo de 'unknown' por cada columna -----")
    df_unknowns.show()
    
    # Extraemos la fila de conteos para presentar un reporte final más limpio
    row_counts = df_unknowns.collect()[0]
    
    print("----- Resumen de variables con valores desconocidos -----")
    encontrados = False
    for column in df_final.columns:
        if row_counts[column] > 0:
            encontrados = True
            print(f"- {column}: {row_counts[column]} registros desconocidos")
            
    if not encontrados:
        print("No se encontraron registros con valor 'unknown' en ninguna variable.")

except Exception as e:
    print(f"Ocurrió un error al ejecutar la consulta: {e}")
    
finally:
    # Finalizar la sesión de Spark
    spark.stop()
