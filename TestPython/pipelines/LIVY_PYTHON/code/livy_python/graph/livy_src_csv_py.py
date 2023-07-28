from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def livy_src_csv_py(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("year", StringType(), True), StructField("industry_code_ANZSIC", StringType(), True), StructField("industry_name_ANZSIC", StringType(), True), StructField("rme_size_grp", StringType(), True), StructField("variable", StringType(), True), StructField("value", StringType(), True), StructField("unit", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("file:/storage/workflowdata/annual-enterprise")
