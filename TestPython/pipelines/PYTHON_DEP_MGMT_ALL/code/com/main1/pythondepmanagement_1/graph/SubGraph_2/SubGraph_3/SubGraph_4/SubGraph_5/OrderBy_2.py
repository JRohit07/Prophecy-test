from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def OrderBy_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        col("`c- short`").asc(), 
        col("`c  - int`").asc(), 
        col("`- c long`").asc(), 
        col("`c_decimal  -  `").asc(), 
        col("`c_float-__  `").asc(), 
        col("`c -  boolean _  `").asc(), 
        col("c_double").asc(), 
        col("`c-string`").asc(), 
        col("`c_date-for today`").asc(), 
        col("`c_timestamp  __ for--today`").asc(), 
        col("p_long").asc(), 
        col("p_decimal").asc(), 
        col("p_float").asc(), 
        col("p_boolean").asc(), 
        col("p_double").asc(), 
        col("p_string").asc(), 
        col("p_date").asc(), 
        col("p_timestamp").asc()
    )
