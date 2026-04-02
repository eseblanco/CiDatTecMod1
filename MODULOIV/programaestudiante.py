import sys
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

def procesar_total_viajes(df):
    """
    Recibe un dataframe con ['identificador', 'viajes'] (viajes es array de structs).
    Retorna dataframe con ['codigo_postal', 'tipo', 'total_viajes'].
    tipo = 'origen' o 'destino'
    """
    if "viajes" not in df.columns:
        # En caso de que el esquema difiera por JSON vacío
        spark = df.sparkSession
        return spark.createDataFrame([], "codigo_postal string, tipo string, total_viajes long")

    df_exploded = df.select(F.explode('viajes').alias('viaje'))
    
    # Origen
    df_origen = df_exploded.select(
        F.col('viaje.codigo_postal_origen').alias('codigo_postal'),
        F.lit('origen').alias('tipo')
    )
    
    # Destino
    df_destino = df_exploded.select(
        F.col('viaje.codigo_postal_destino').alias('codigo_postal'),
        F.lit('destino').alias('tipo')
    )
    
    df_union = df_origen.unionAll(df_destino)
    df_totales = df_union.groupBy('codigo_postal', 'tipo').agg(F.count('*').alias('total_viajes'))
    return df_totales


def procesar_total_ingresos(df):
    """
    Retorna dataframe con ['codigo_postal', 'tipo', 'ingresos']
    ingreso = kilometros * precio_kilometro
    """
    if "viajes" not in df.columns:
        spark = df.sparkSession
        return spark.createDataFrame([], "codigo_postal string, tipo string, ingresos double")

    df_exploded = df.select(F.explode('viajes').alias('viaje'))
    df_exploded = df_exploded.withColumn('ingreso', F.col('viaje.kilometros').cast('double') * F.col('viaje.precio_kilometro').cast('double'))
    
    # Origen
    df_origen = df_exploded.select(
        F.col('viaje.codigo_postal_origen').alias('codigo_postal'),
        F.lit('origen').alias('tipo'),
        F.col('ingreso')
    )
    
    # Destino
    df_destino = df_exploded.select(
        F.col('viaje.codigo_postal_destino').alias('codigo_postal'),
        F.lit('destino').alias('tipo'),
        F.col('ingreso')
    )
    
    df_union = df_origen.unionAll(df_destino)
    df_totales = df_union.groupBy('codigo_postal', 'tipo').agg(F.sum('ingreso').alias('ingresos'))
    return df_totales


def procesar_metricas(df):
    """
    Retorna dataframe con ['metrica', 'valor']
    """
    spark = df.sparkSession
    if "viajes" not in df.columns:
        metricas_vacias = [
            ("persona_con_mas_kilometros", ""),
            ("persona_con_mas_ingresos", ""),
            ("percentil_25", "0.0"),
            ("percentil_50", "0.0"),
            ("percentil_75", "0.0"),
            ("codigo_postal_origen_con_mas_ingresos", ""),
            ("codigo_postal_destino_con_mas_ingresos", "")
        ]
        return spark.createDataFrame(metricas_vacias, ["metrica", "valor"])

    df_exploded = df.select('identificador', F.explode('viajes').alias('viaje'))
    df_exploded = df_exploded.withColumn('kilometros', F.col('viaje.kilometros').cast('double')) \
                             .withColumn('ingreso', F.col('viaje.kilometros').cast('double') * F.col('viaje.precio_kilometro').cast('double'))
    
    # persona_con_mas_kilometros
    df_km_persona = df_exploded.groupBy('identificador').agg(F.sum('kilometros').alias('total_km'))
    persona_mas_km = df_km_persona.orderBy(F.col('total_km').desc()).first()
    persona_mas_km_id = persona_mas_km['identificador'] if persona_mas_km else ""
    
    # persona_con_mas_ingresos
    df_ingreso_persona = df_exploded.groupBy('identificador').agg(F.sum('ingreso').alias('total_ingreso'))
    persona_mas_ingreso = df_ingreso_persona.orderBy(F.col('total_ingreso').desc()).first()
    persona_mas_ingreso_id = persona_mas_ingreso['identificador'] if persona_mas_ingreso else ""
    
    # percentiles (percentil_25, percentil_50, percentil_75)
    if df_ingreso_persona.count() > 0:
        percentiles = df_ingreso_persona.approxQuantile("total_ingreso", [0.25, 0.5, 0.75], 0.0)
        p25, p50, p75 = percentiles
    else:
        p25, p50, p75 = 0.0, 0.0, 0.0
        
    # codigo_postal_origen_con_mas_ingresos
    df_cp_origen = df_exploded.groupBy(F.col('viaje.codigo_postal_origen').alias('codigo_postal')).agg(F.sum('ingreso').alias('ingreso_origen'))
    cp_origen = df_cp_origen.orderBy(F.col('ingreso_origen').desc()).first()
    cp_origen_val = cp_origen['codigo_postal'] if cp_origen else ""
    
    # codigo_postal_destino_con_mas_ingresos
    df_cp_destino = df_exploded.groupBy(F.col('viaje.codigo_postal_destino').alias('codigo_postal')).agg(F.sum('ingreso').alias('ingreso_destino'))
    cp_destino = df_cp_destino.orderBy(F.col('ingreso_destino').desc()).first()
    cp_destino_val = cp_destino['codigo_postal'] if cp_destino else ""
    
    # Crear dataframe con las métricas
    metricas = [
        ("persona_con_mas_kilometros", str(persona_mas_km_id)),
        ("persona_con_mas_ingresos", str(persona_mas_ingreso_id)),
        ("percentil_25", str(p25)),
        ("percentil_50", str(p50)),
        ("percentil_75", str(p75)),
        ("codigo_postal_origen_con_mas_ingresos", str(cp_origen_val)),
        ("codigo_postal_destino_con_mas_ingresos", str(cp_destino_val))
    ]
    
    return spark.createDataFrame(metricas, ["metrica", "valor"])

def main():
    if len(sys.argv) < 2:
        print("Uso: spark-submit programaestudiante.py persona*.json")
        sys.exit(1)
        
    input_files = sys.argv[1:]
    
    spark = SparkSession.builder.appName("Tarea2-BigData").getOrCreate()
    
    # Leer JSON
    df = spark.read.option("multiline", "true").json(input_files)
    
    df_viajes = procesar_total_viajes(df)
    df_ingresos = procesar_total_ingresos(df)
    df_metricas = procesar_metricas(df)
    
    # Guardar como CSV
    df_viajes.coalesce(1).write.option("header", "true").csv("total_viajes.csv", mode="overwrite")
    df_ingresos.coalesce(1).write.option("header", "true").csv("total_ingresos.csv", mode="overwrite")
    df_metricas.coalesce(1).write.option("header", "true").csv("metricas.csv", mode="overwrite")
    
    spark.stop()

if __name__ == "__main__":
    main()
