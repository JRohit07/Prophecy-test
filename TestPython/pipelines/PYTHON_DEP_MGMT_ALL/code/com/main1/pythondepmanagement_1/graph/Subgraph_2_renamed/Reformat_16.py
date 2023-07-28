from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Reformat_16(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(concat(lit(Config.c_sg2_config1), col("c_short")).alias("c_config"))
