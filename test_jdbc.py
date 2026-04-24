from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Test").config("spark.jars.packages", "org.postgresql:postgresql:42.5.4").getOrCreate()
try:
    driver = spark._jvm.org.postgresql.Driver()
    print("Driver instantiated successfully:", driver)
except Exception as e:
    print("Error:", e)
spark.stop()
