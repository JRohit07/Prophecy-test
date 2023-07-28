from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from perf_unitest_generate.config.ConfigStore import *
from perf_unitest_generate.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("country_code"))

    return df1.agg(
        first(col("account_flags_renamed")).alias("account_flags_renamed"), 
        first(col("account_open_date")).alias("account_open_date")
    )
