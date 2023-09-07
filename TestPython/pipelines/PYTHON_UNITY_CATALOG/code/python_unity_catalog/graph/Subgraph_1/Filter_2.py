from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from python_unity_catalog.udfs.UDFs import *

def Filter_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(lit(True))
