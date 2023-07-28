from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def Reformat_3(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("firstname"), 
        col("middlename"), 
        col("lastname"), 
        col("id"), 
        col("salary"), 
        col("processed"), 
        col("dob"), 
        col("weight"), 
        col("state"), 
        col("city"), 
        col("gender")
    )
