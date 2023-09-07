from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def parse_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("coin"), 
        col("currency"), 
        col("content_parsed.rate").alias("rate"), 
        col("content_parsed.time").alias("time")
    )
