from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from python_one_gem_only.config.ConfigStore import *
from python_one_gem_only.udfs.UDFs import *

def Reformat_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0
