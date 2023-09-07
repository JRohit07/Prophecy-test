from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_22(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c- short`").alias("c_short"), 
        col("`c  - int`").alias("c_int"), 
        col("`- c long`").alias("c_long"), 
        col("`c_decimal  -  `").alias("c_decimal"), 
        col("`c_float-__  `").alias("c_float"), 
        col("`c -  boolean _  `").alias("c_boolean"), 
        col("c_double"), 
        col("`c-string`").alias("c_string")
    )
