from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasicio.test.mainone.config.ConfigStore import *
from pythonbasicio.test.mainone.udfs.UDFs import *

def Script_4(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print("hello")
    out0 = in0

    return out0
