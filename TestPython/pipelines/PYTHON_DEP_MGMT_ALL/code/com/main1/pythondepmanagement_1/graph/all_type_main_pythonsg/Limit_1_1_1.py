from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Limit_1_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(100)
