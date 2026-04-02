import pytest
from pyspark.sql import SparkSession
from programaestudiante import procesar_total_viajes, procesar_total_ingresos, procesar_metricas

@pytest.fixture(scope="session")
def spark():
    spark_session = SparkSession.builder \
        .appName("pytest-pyspark-testing") \
        .master("local[1]") \
        .getOrCreate()
    yield spark_session
    spark_session.stop()

def test_procesar_total_viajes(spark):
    json_data = [
        '{"identificador": "1", "viajes": [{"codigo_postal_origen": "11504", "codigo_postal_destino": "11501", "kilometros": "2.8", "precio_kilometro": "550"}, {"codigo_postal_origen": "11504", "codigo_postal_destino": "10101", "kilometros": "5.0", "precio_kilometro": "500"}]}',
        '{"identificador": "2", "viajes": [{"codigo_postal_origen": "10101", "codigo_postal_destino": "11504", "kilometros": "10.0", "precio_kilometro": "100"}]}'
    ]
    rdd = spark.sparkContext.parallelize(json_data)
    df = spark.read.json(rdd)
    
    df_res = procesar_total_viajes(df)
    res = { (row['codigo_postal'], row['tipo']): row['total_viajes'] for row in df_res.collect() }
    
    # Verificaciones
    assert res.get(("11504", "origen")) == 2
    assert res.get(("11501", "destino")) == 1
    assert res.get(("10101", "destino")) == 1
    assert res.get(("10101", "origen")) == 1
    assert res.get(("11504", "destino")) == 1

def test_procesar_total_ingresos(spark):
    json_data = [
        '{"identificador": "1", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "2.0", "precio_kilometro": "50"}]}',  # ingreso = 100
        '{"identificador": "2", "viajes": [{"codigo_postal_origen": "B", "codigo_postal_destino": "A", "kilometros": "3.0", "precio_kilometro": "100"}]}' # ingreso = 300
    ]
    rdd = spark.sparkContext.parallelize(json_data)
    df = spark.read.json(rdd)
    
    df_res = procesar_total_ingresos(df)
    res = { (row['codigo_postal'], row['tipo']): row['ingresos'] for row in df_res.collect() }
    
    assert res.get(("A", "origen")) == 100.0
    assert res.get(("B", "destino")) == 100.0
    assert res.get(("B", "origen")) == 300.0
    assert res.get(("A", "destino")) == 300.0

def test_procesar_metricas(spark):
    json_data = [
        '{"identificador": "1", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "10.0", "precio_kilometro": "10"}]}',  # km=10, ingreso=100
        '{"identificador": "2", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "C", "kilometros": "20.0", "precio_kilometro": "10"}]}',  # km=20, ingreso=200
        '{"identificador": "3", "viajes": [{"codigo_postal_origen": "B", "codigo_postal_destino": "A", "kilometros": "5.0", "precio_kilometro": "10"}]}'    # km=5, ingreso=50
    ]
    rdd = spark.sparkContext.parallelize(json_data)
    df = spark.read.json(rdd)
    
    df_res = procesar_metricas(df)
    res = { row['metrica']: row['valor'] for row in df_res.collect() }
    
    assert res.get("persona_con_mas_kilometros") == "2"
    assert res.get("persona_con_mas_ingresos") == "2"
    assert res.get("codigo_postal_origen_con_mas_ingresos") == "A"
    assert res.get("codigo_postal_destino_con_mas_ingresos") == "C"

def test_procesar_metricas_percentiles(spark):
    json_data = [
        '{"identificador": "1", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "1.0", "precio_kilometro": "10"}]}',
        '{"identificador": "2", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "1.0", "precio_kilometro": "20"}]}',
        '{"identificador": "3", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "1.0", "precio_kilometro": "30"}]}',
        '{"identificador": "4", "viajes": [{"codigo_postal_origen": "A", "codigo_postal_destino": "B", "kilometros": "1.0", "precio_kilometro": "40"}]}'
    ]
    rdd = spark.sparkContext.parallelize(json_data)
    df = spark.read.json(rdd)
    df_res = procesar_metricas(df)
    res = { row['metrica']: row['valor'] for row in df_res.collect() }
    
    assert 10.0 <= float(res.get("percentil_25", "0.0")) <= 20.0
    assert 20.0 <= float(res.get("percentil_50", "0.0")) <= 30.0
    assert 30.0 <= float(res.get("percentil_75", "0.0")) <= 40.0

def test_empty_json(spark):
    from pyspark.sql.types import StructType, StructField, StringType, ArrayType
    schema = StructType([
        StructField("identificador", StringType(), True),
        StructField("viajes", ArrayType(
            StructType([
                StructField("codigo_postal_origen", StringType(), True),
                StructField("codigo_postal_destino", StringType(), True),
                StructField("kilometros", StringType(), True),
                StructField("precio_kilometro", StringType(), True)
            ])
        ), True)
    ])
    
    json_data = [
        '{"identificador": "1", "viajes": []}',
        '{"identificador": "2"}'
    ]
    rdd = spark.sparkContext.parallelize(json_data)
    df = spark.read.schema(schema).json(rdd)
    
    df_viajes = procesar_total_viajes(df)
    assert df_viajes.count() == 0
    
    df_ingresos = procesar_total_ingresos(df)
    assert df_ingresos.count() == 0

    df_metricas = procesar_metricas(df)
    assert df_metricas.count() == 7
