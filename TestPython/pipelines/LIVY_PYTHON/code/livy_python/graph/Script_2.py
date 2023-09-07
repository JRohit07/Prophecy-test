from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def Script_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    # from fast_html import render,p
    # print(render(p("text")))
    out0 = in0

    return out0
