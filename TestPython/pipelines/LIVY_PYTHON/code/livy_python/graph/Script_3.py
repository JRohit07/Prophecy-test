from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def Script_3(spark: SparkSession, in0: DataFrame):
    out0 = in0
    out1 = in0.filter(col("year") >= 2010)
    out1.show()

    return 
