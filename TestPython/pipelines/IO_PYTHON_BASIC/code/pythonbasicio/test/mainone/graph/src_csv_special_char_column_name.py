from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasicio.test.mainone.config.ConfigStore import *
from pythonbasicio.test.mainone.udfs.UDFs import *

def src_csv_special_char_column_name(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("c   short  --", StringType(), True), StructField("c-int-column type", StringType(), True), StructField("-- c-long", StringType(), True), StructField("c-decimal", StringType(), True), StructField("c  float", StringType(), True), StructField("c--boolean", StringType(), True), StructField("c- - -double", StringType(), True), StructField("c___-- string", StringType(), True), StructField("c  date", StringType(), True), StructField("c_timestamp", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Prophecy/qa_data/csv/special_char_column_name")
