from pyspark.sql import SparkSession

# 1. Inicializar sesión de Spark
# Se incluye el paquete JDBC de PostgreSQL necesario para la conexión
spark = (
    SparkSession.builder.appName("CreacionTablasPostgres")
    .config("spark.jars.packages", "org.postgresql:postgresql:42.5.4")
    .getOrCreate()
)

# 2. Configuración de la conexión a la base de datos
url = "jdbc:postgresql://localhost:5432/postgres"
user = "root"
password = "sdbz.jvj1"

# 3. Script SQL proporcionado
sql_script = """
-- 1. Crear el esquema si no existe
CREATE SCHEMA IF NOT EXISTS tarea3;

-- 2. Crear tabla de Educación (Catálogo)
CREATE TABLE tarea3.education (
    codigo INT PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

-- 3. Crear tabla de Trabajos / Empleos (Catálogo)
CREATE TABLE tarea3.jobs (
    codigo INT PRIMARY KEY,
    descripcion VARCHAR(50) NOT NULL
);

-- 4. Crear tabla principal (bank_sample)
-- Se incluye un ID serial como llave primaria para integridad referencial
CREATE TABLE tarea3.bank_sample (
    id SERIAL PRIMARY KEY,
    age INT,
    job_id INT,
    marital VARCHAR(20),
    education_id INT,
    "default" VARCHAR(5),
    balance INT,
    housing VARCHAR(5),
    loan VARCHAR(5),
    contact VARCHAR(20),
    day INT,
    month VARCHAR(10),
    duration INT,
    campaign INT,
    pdays INT,
    previous INT,
    poutcome VARCHAR(20),
    y VARCHAR(5),
    
    -- 5. Crear las relaciones (Foreign Keys)
    CONSTRAINT fk_job 
        FOREIGN KEY (job_id) 
        REFERENCES tarea3.jobs(codigo),
        
    CONSTRAINT fk_education 
        FOREIGN KEY (education_id) 
        REFERENCES tarea3.education(codigo)
);
"""

# 4. Ejecución del script DDL
# Para ejecutar sentencias DDL (como CREATE TABLE) utilizamos el acceso a la JVM de PySpark,
# ya que las APIs nativas de DataFrame de Spark están enfocadas al manejo (DML) de datos.
try:
    # Obtener el driver de PostgreSQL explícitamente para evitar problemas de ClassLoader
    # con el DriverManager cuando se carga por medio de 'spark.jars.packages'
    driver = spark._jvm.org.postgresql.Driver()

    # Configurar las propiedades de la conexión
    properties = spark._jvm.java.util.Properties()
    properties.setProperty("user", user)
    properties.setProperty("password", password)

    # Establecer la conexión JDBC usando el driver instanciado directamente
    connection = driver.connect(url, properties)

    # Crear el Statement y ejecutar el script
    statement = connection.createStatement()
    statement.execute(sql_script)

    print(
        "El script SQL ha sido ejecutado con éxito. Esquema y tablas creadas en PostgreSQL."
    )

except Exception as e:
    print(f"Ocurrió un error al ejecutar el script: {e}")

finally:
    # Asegurarse de cerrar la conexión y el statement
    if "statement" in locals() and statement is not None:
        statement.close()
    if "connection" in locals() and connection is not None:
        connection.close()

# Finalizar la sesión de Spark
spark.stop()
