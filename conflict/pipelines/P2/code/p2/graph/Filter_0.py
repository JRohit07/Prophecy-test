from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p2.config.ConfigStore import *
from p2.udfs.UDFs import *

def Filter_0(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(lit(True))
