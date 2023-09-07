from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasicio.test.mainone.config.ConfigStore import *
from pythonbasicio.test.mainone.udfs.UDFs import *

def Reformat_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c   short  --`"), 
        col("`c-int-column type`"), 
        col("`-- c-long`"), 
        col("`c-decimal`"), 
        col("`c  float`"), 
        col("`c--boolean`"), 
        col("`c- - -double`"), 
        concat(col("`c___-- string`"), lit(Config.c_string)).alias("`c___-- string`"), 
        col("`c  date`"), 
        col("c_timestamp")
    )
