from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def parse(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("method"), 
        col("url"), 
        col("json"), 
        col("headers"), 
        col("params"), 
        col("api_output.status_code").alias("status_code"), 
        col("api_output.reason").alias("reason"), 
        col("api_output.content").alias("content")
    )
