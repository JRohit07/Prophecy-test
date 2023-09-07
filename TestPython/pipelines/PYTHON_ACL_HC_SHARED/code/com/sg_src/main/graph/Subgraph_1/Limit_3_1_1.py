from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from com.sg_src.main.udfs.UDFs import *

def Limit_3_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(10)
