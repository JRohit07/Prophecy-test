from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Reformat_3(spark: SparkSession, in0: DataFrame) -> DataFrame:
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
        col("`c_array-int  _ int`"), 
        col("`c_array-string  _ string`"), 
        col("`c_array--long`"), 
        col("`c_array-- boolean `"), 
        col("`-- c_array_timestamp -- `"), 
        col("`c_array -- float`"), 
        col("`c_array -- decimal`"), 
        col("`c_struct -- _  `"), 
        col("p_short"), 
        col("p_int"), 
        col("p_long"), 
        col("p_decimal"), 
        col("p_float"), 
        col("p_boolean"), 
        col("p_double"), 
        col("p_string"), 
        col("p_date"), 
        col("p_timestamp")
    )
