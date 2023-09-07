from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from python_streaming_main.udfs.UDFs import *

def WindowFunction_1_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn(
          "c_float-__  ",
          row_number()\
            .over(Window\
            .partitionBy(
              col("c_double"), 
              col("`c- short`"), 
              col("`- c long`"), 
              col("c_decimal_new"), 
              col("`c_float-__  `"), 
              col("`c -  boolean _  `"), 
              col("`c-string`"), 
              col("`c_date-for today`"), 
              col("`c_timestamp  __ for--today`"), 
              col("p_short"), 
              col("p_int"), 
              col("p_long"), 
              col("p_decimal"), 
              col("p_float"), 
              col("p_boolean"), 
              col("p_double"), 
              col("p_string"), 
              col("p_date"), 
              col("p_timestamp"), 
              col("c_double_c_float")
            )\
            .orderBy(col("c_double").asc(), col("`c- short`").asc()))
        )\
        .withColumn("c_date-for today", row_number()\
        .over(Window\
        .partitionBy(
          col("c_double"), 
          col("`c- short`"), 
          col("`- c long`"), 
          col("c_decimal_new"), 
          col("`c_float-__  `"), 
          col("`c -  boolean _  `"), 
          col("`c-string`"), 
          col("`c_date-for today`"), 
          col("`c_timestamp  __ for--today`"), 
          col("p_short"), 
          col("p_int"), 
          col("p_long"), 
          col("p_decimal"), 
          col("p_float"), 
          col("p_boolean"), 
          col("p_double"), 
          col("p_string"), 
          col("p_date"), 
          col("p_timestamp"), 
          col("c_double_c_float")
        )\
        .orderBy(col("c_double").asc(), col("`c- short`").asc())))
