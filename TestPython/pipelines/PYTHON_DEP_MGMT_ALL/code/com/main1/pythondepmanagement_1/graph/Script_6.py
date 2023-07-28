from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Script_6(
        spark: SparkSession, 
        in0: DataFrame, 
        in1: DataFrame, 
        in2: DataFrame, 
        in3: DataFrame, 
        in4: DataFrame, 
        in5: DataFrame, 
        in6: DataFrame
) -> DataFrame:
    c_test_var_init = c_int + c_float
    out00 = in0.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out1 = in1.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out2 = in2.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out3 = in3.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out4 = in4.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out5 = in5.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out6 = in6.select("c-string").withColumnRenamed("c-string", "c_str_new")
    out0 = out00.union(out1).union(out2).union(out3).union(out4).union(out5).union(out6)

    return out0
