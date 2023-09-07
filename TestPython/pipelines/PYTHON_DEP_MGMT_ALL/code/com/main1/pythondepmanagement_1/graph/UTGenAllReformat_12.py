from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def UTGenAllReformat_12(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c- short`"), 
        col("`c  - int`"), 
        col("`- c long`"), 
        col("`c_decimal  -  `"), 
        col("`c_float-__  `"), 
        col("`c -  boolean _  `"), 
        col("c_double"), 
        col("`c-string`"), 
        col("`c_date-for today`"), 
        col("`c_timestamp  __ for--today`"), 
        col("`c-bytes`"), 
        col("`c-binary`"), 
        col("p_date")
    )
