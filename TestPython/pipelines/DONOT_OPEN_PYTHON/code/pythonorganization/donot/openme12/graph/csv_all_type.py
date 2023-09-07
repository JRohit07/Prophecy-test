from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def csv_all_type(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("_c0", StringType(), True), StructField("_c1", StringType(), True), StructField("_c2", StringType(), True), StructField("_c3", StringType(), True), StructField("_c4", StringType(), True), StructField("_c5", StringType(), True), StructField("_c6", StringType(), True), StructField("_c7", StringType(), True), StructField("_c8", StringType(), True), StructField("_c9", StringType(), True)
        ])
        )\
        .option("header", False)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/qa_data/csv/all_type_no_partition")
