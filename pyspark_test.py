from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder \
    .appName("TestApp") \
    .getOrCreate()

print("✅ Spark Session started successfully")
print("Spark version:", spark.version)

# Simple test DataFrame
df = spark.range(5)
df.show()

spark.stop()
