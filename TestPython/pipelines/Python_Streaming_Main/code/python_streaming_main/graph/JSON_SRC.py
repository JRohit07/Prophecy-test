from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def JSON_SRC(spark: SparkSession) -> DataFrame:
    return spark.readStream\
        .format("json")\
        .option("latestFirst", True)\
        .option("primitivesAsString", True)\
        .option("allowUnquotedFieldNames", False)\
        .option("allowSingleQuotes", True)\
        .option("allowNumericLeadingZeros", True)\
        .option("allowBackslashEscapingAnyCharacter", True)\
        .option("dropFieldIfAllNull", False)\
        .option("maxFilesPerTrigger", "1")\
        .option("maxFileAge", "1")\
        .schema(
          StructType([
            StructField("c_array", ArrayType(StringType(), True), True), StructField("c_bigint", LongType(), True), StructField("c_boolean", BooleanType(), True), StructField("c_double", DoubleType(), True), StructField("c_float", DoubleType(), True), StructField("c_int", LongType(), True), StructField("c_smallint", LongType(), True), StructField("c_string", StringType(), True), StructField("c_struct", StructType([
              StructField("city", StringType(), True), StructField("pin", StringType(), True), StructField("state", StringType(), True)
            ]), True), StructField("c_tinyint", LongType(), True), StructField("p_int", IntegerType(), True), StructField("p_float", DoubleType(), True), StructField("p_string", StringType(), True)
        ])
        )\
        .load("dbfs:/Prophecy/qa_data/streaming/json/all_type_with_partition")
