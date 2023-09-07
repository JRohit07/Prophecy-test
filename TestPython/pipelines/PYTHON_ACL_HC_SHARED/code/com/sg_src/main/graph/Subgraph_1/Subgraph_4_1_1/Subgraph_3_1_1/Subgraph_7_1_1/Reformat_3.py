from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from com.sg_src.main.udfs.UDFs import *

def Reformat_3(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(squared(lit(5)), factorial(lit(2)), random_string(lit(4)), col("`c-string`"), lit(Config.c_sg7_1_1_short))\
          .alias("c_udf"), 
        col("`c-string`").alias("c-string"), 
        col("c_udf_usage")
    )
