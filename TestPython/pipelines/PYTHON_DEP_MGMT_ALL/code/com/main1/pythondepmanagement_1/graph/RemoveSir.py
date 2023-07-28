from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def RemoveSir(spark: SparkSession, in0: DataFrame, in1: DataFrame) -> (DataFrame, DataFrame):
    out0 = in0
    out1 = in1

    return (out0, out1)
