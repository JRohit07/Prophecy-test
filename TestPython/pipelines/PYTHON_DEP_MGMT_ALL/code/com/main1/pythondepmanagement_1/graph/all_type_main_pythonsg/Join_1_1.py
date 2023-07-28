from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Join_1_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.`- c long`") == col("in1.`- c long`")), "inner")\
        .select(col("in0.`c- short`").alias("c- short"), col("in0.`c  - int`").alias("c  - int"), col("in0.`- c long`").alias("- c long"), col("in0.`c_decimal  -  `").alias("c_decimal  -  "), col("in0.`c_float-__  `").alias("c_float-__  "), col("in0.`c -  boolean _  `").alias("c -  boolean _  "), col("in0.c_double").alias("c_double"), col("in0.`c-string`").alias("c-string"), col("in0.`c_date-for today`").alias("c_date-for today"), col("in0.`c_timestamp  __ for--today`").alias("c_timestamp  __ for--today"), col("in0.`c_array-int  _ int`").alias("c_array-int  _ int"), col("in0.`c_array-string  _ string`").alias("c_array-string  _ string"), col("in0.`c_array--long`").alias("c_array--long"), col("in0.`c_array-- boolean `").alias("c_array-- boolean "), col("in0.`-- c_array_timestamp -- `").alias("-- c_array_timestamp -- "), col("in0.`c_array -- float`").alias("c_array -- float"), col("in0.`c_array -- decimal`").alias("c_array -- decimal"), col("in0.`c_struct -- _  `").alias("c_struct -- _  "), col("in0.p_short").alias("p_short"), col("in0.p_int").alias("p_int"), col("in0.p_long").alias("p_long"), col("in0.p_decimal").alias("p_decimal"), col("in0.p_float").alias("p_float"), col("in0.p_boolean").alias("p_boolean"), col("in0.p_double").alias("p_double"), col("in0.p_string").alias("p_string"), col("in0.p_date").alias("p_date"), col("in0.p_timestamp").alias("p_timestamp"))
