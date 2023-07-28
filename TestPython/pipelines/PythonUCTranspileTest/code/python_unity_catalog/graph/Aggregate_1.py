from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def Aggregate_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("middlename"), col("lastname"))

    return df1.agg(
        first(col("firstname")).alias("firstname"), 
        first(col("id")).alias("id"), 
        first(col("salary")).alias("salary"), 
        first(col("processed")).alias("processed"), 
        first(col("dob")).alias("dob"), 
        first(col("weight")).alias("weight"), 
        first(col("state")).alias("state"), 
        first(col("city")).alias("city"), 
        first(col("gender")).alias("gender")
    )
