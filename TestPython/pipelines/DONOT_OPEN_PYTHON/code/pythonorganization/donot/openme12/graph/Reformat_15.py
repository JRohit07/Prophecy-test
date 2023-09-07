from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Reformat_15(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("_c0"), 
        col("_c1"), 
        col("_c2"), 
        col("_c3"), 
        col("_c4"), 
        col("_c5"), 
        col("_c6"), 
        col("_c7"), 
        col("_c8"), 
        col("_c9")
    )
