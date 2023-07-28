from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def Script_3(spark: SparkSession, in0: DataFrame) -> DataFrame:
    raise Exception("Sorry, sir a blocking exception buddy")
    out0 = in0

    return out0
