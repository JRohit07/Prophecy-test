from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Reformat_10(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(concat(lit(Config.c_sg2_c_string), lit("b")).alias("c_config"))
