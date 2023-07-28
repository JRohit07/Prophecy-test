from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(squared(lit(5)), factorial(lit(2)), random_string(lit(4))).alias("c_udfs_usage"), 
        col("`c-string`").alias("c-string")
    )
