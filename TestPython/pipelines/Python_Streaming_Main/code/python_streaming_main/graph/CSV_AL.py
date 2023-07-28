from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def CSV_AL(spark: SparkSession) -> DataFrame:
    return spark.readStream\
        .format("cloudFiles")\
        .option("cloudFiles.format", "csv")\
        .option("cloudFiles.allowOverwrites", True)\
        .option("ignoreCorruptFiles", True)\
        .option("header", True)\
        .option("sep", ",")\
        .schema(
          StructType([
            StructField("c_tinyint", StringType(), True), StructField("c_smallint", StringType(), True), StructField("c_int", StringType(), True), StructField("c_bigint", StringType(), True), StructField("c_float", StringType(), True), StructField("c_double", StringType(), True), StructField("c_string", StringType(), True), StructField("c_boolean", StringType(), True), StructField("p_int", IntegerType(), True), StructField("p_float", DoubleType(), True), StructField("p_string", StringType(), True)
        ])
        )\
        .load("dbfs:/Prophecy/qa_data/streaming/csv/all_type_with_partition")
