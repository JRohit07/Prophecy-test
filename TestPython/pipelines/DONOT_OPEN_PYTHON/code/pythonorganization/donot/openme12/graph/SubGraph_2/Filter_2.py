from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Filter_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("`c-string`").like("%"))
