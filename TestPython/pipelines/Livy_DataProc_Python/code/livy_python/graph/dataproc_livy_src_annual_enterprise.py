from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def dataproc_livy_src_annual_enterprise(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("year", StringType(), True), StructField("industry_code_ANZSIC", StringType(), True), StructField("industry_name_ANZSIC", StringType(), True), StructField("rme_size_grp", StringType(), True), StructField("variable", StringType(), True), StructField("value", StringType(), True), StructField("unit", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("gs://qa-prophecy/default_datasets/annual-enterprise")
