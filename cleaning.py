from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, round
from pyspark.sql.types import IntegerType, DateType
import os

#cria uma sessão spark

spark = SparkSession.builder.appName("DataCleaning").config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2").config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.InstanceProfileCredentialsProvider").getOrCreate()

file_path = "VRA_20240916110513.csv"

df = spark.read.csv(file_path, header=True, sep=";")

#mostrar apenas o header

df.show(1)