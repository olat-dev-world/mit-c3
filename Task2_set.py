 
# Import
from pyspark.sql import SparkSession
import random

appName = "Audio_and_Video_call"+str(random.randrange(10,200))

# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName(appName).getOrCreate()

# Read CSV 
options = {
    "inferSchema": "False",
    "delimiter": ",",
    "header":"True"
}

csv_data = f'c:/test/ipdv.csv'
df_csv = spark.read.csv(csv_data)

# df = spark.read.csv("ipdr.csv")
# df.printSchema()