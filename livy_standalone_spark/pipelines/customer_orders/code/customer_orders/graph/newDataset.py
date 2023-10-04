from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from customer_orders.config.ConfigStore import *
from customer_orders.udfs.UDFs import *

def newDataset(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("year", StringType(), True), StructField("industry_code_ANZSIC", StringType(), True), StructField("industry_name_ANZSIC", StringType(), True), StructField("rme_size_grp", StringType(), True), StructField("variable", StringType(), True), StructField("value", StringType(), True), StructField("unit", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("file:/storage/workflowdata/annual-enterprise")
