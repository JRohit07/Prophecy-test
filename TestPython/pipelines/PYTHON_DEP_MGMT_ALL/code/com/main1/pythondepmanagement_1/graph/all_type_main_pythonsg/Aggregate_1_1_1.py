from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Aggregate_1_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("c_double"))

    return df1.agg(
        first(col("`c- short`")).alias("c- short"), 
        first(col("`c  - int`")).alias("c  - int"), 
        first(col("`- c long`")).alias("- c long"), 
        first(col("`c_decimal  -  `")).alias("c_decimal  -  "), 
        first(col("`c_float-__  `")).alias("c_float-__  "), 
        first(col("`c -  boolean _  `")).alias("c -  boolean _  "), 
        first(col("`c-string`")).alias("c-string"), 
        first(col("`c_date-for today`")).alias("c_date-for today"), 
        first(col("`c_timestamp  __ for--today`")).alias("c_timestamp  __ for--today"), 
        first(col("`c_array-int  _ int`")).alias("c_array-int  _ int"), 
        first(col("`c_array-string  _ string`")).alias("c_array-string  _ string"), 
        first(col("`c_array--long`")).alias("c_array--long"), 
        first(col("`c_array-- boolean `")).alias("c_array-- boolean "), 
        first(col("`-- c_array_timestamp -- `")).alias("-- c_array_timestamp -- "), 
        first(col("`c_array -- float`")).alias("c_array -- float"), 
        first(col("`c_array -- decimal`")).alias("c_array -- decimal"), 
        first(col("`c_struct -- _  `")).alias("c_struct -- _  "), 
        first(col("p_short")).alias("p_short"), 
        first(col("p_int")).alias("p_int"), 
        first(col("p_long")).alias("p_long"), 
        first(col("p_decimal")).alias("p_decimal"), 
        first(col("p_float")).alias("p_float"), 
        first(col("p_boolean")).alias("p_boolean"), 
        first(col("p_double")).alias("p_double"), 
        first(col("p_string")).alias("p_string"), 
        first(col("p_date")).alias("p_date"), 
        first(col("p_timestamp")).alias("p_timestamp")
    )
