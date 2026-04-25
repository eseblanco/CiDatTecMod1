from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, desc

# 1. Inicializar sesión de Spark
spark = (
    SparkSession.builder.appName("ImputarModaContact")
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


    # 3. Cargar el set de datos
print("Cargando el set de datos desde PostgreSQL...")
df_bank = spark.read.jdbc(url=url, table="tarea3.bank", properties=jdbc_properties)
df_jobs = spark.read.jdbc(url=url, table="tarea3.jobs", properties=jdbc_properties)
df_education = spark.read.jdbc(url=url, table="tarea3.education", properties=jdbc_properties)

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



moda_row = df_final.filter(col("contact") != "unknown") \
                       .groupBy("contact") \
                       .count() \
                       .orderBy(desc("count")) \
                       .first()
                       
if moda_row:
    moda_contact = moda_row["contact"]
    print(f"La moda calculada es: '{moda_contact}'")
        
    # 5. Imputar la variable 'contact'
    print(f"\nSustituyendo los valores 'unknown' por '{moda_contact}'...")
    df_final = df_final.withColumn(
        "contact", 
        when(col("contact") == "unknown", moda_contact).otherwise(col("contact"))
    )
        
    # 6. Mostrar el resultado para verificar la imputación
    print("\n----- Distribución de la variable 'contact' DESPUÉS de la imputación -----")
    df_final.groupBy("contact").count().show()
else:
    print("No se pudo calcular la moda ya que no hay valores válidos en la columna 'contact'.")


# imputación de las variable education. 

moda_edu_row = df_final.filter(col("education") != "unknown") \
                 .groupBy("education") \
                 .count() \
                 .orderBy(desc("count")) \
                 .first()
                 
if moda_edu_row:
    moda_edu_val = moda_edu_row["education"]
    print(f"La moda calculada para 'education' es: '{moda_edu_val}'")
       
    print(f"Sustituyendo los valores 'unknown' por '{moda_edu_val}'...")
    df_final = df_final.withColumn(
        "education", 
        when(col("education") == "unknown", moda_edu_val).otherwise(col("education"))
    )
        
    print("Distribución de 'education' DESPUÉS de la imputación:")
    df_final.groupBy("education").count().show()
else:
    print("No se pudo calcular la moda para 'education'.")

# imputación de las variable job . 
print("\nCalculando la moda para la variable 'job'...")
moda_job_row = df_final.filter(col("job") != "unknown") \
            .groupBy("job") \
            .count() \
            .orderBy(desc("count")) \
            .first()
                 
if moda_job_row:
    moda_job_val = moda_job_row["job"]
    print(f"La moda calculada para 'job' es: '{moda_job_val}'")
    
    print(f"Sustituyendo los valores 'unknown' por '{moda_job_val}'...")
    df_final = df_final.withColumn(
       "job", 
       when(col("job") == "unknown", moda_job_val).otherwise(col("job"))
    )
        
    print("Distribución de 'job' DESPUÉS de la imputación:")
    df_final.groupBy("job").count().show()
else:
    print("No se pudo calcular la moda para 'job'.")

# Guardar el DataFrame resultante a un archivo CSV
print("\nGuardando el set de datos final en 'final.csv'...")
# Usamos coalesce(1) para forzar que Spark escriba un único archivo CSV en lugar de múltiples particiones
df_final.coalesce(1).write.csv("final.csv", header=True, mode="overwrite")
print("Archivo guardado exitosamente.")

# Finalizar la sesión de Spark
spark.stop()
