from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from perf_unitest_generate.config.ConfigStore import *
from perf_unitest_generate.udfs.UDFs import *

def WindowFunction_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withColumn(
        "country_code",
        row_number().over(Window.partitionBy(col("account_flags_renamed")).orderBy(col("account_open_date").asc()))
    )
