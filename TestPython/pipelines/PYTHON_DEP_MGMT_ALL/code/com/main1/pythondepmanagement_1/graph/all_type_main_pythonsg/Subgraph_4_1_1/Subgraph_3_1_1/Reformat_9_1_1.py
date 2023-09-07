from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_9_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c-string`"), 
        concat(
            squared(lit(5)), 
            factorial(lit(2)), 
            random_string(lit(4)), 
            lit(Config.c_sg3_1_1_c_long), 
            lit(Config.c_string)
          )\
          .alias("c_udf_usage")
    )
