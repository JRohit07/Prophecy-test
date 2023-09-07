from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    concatstring = (
        str(Config.c_boolean)
        + str(Config.c_double)
        + str(Config.c_float)
        + str(Config.c_int)
        + str(Config.c_long)
        + str(Config.c_short)
        + str(Config.c_string1)
        + str(Config.c_repartition_expr)
        + str(Config.c_0)
    )
    print(f"Concatednated value is: {concatstring}")
    a = int(Config.c_1)
    b = int(Config.c_0)
    real_val = a * b
    assert (real_val == 0)
    out0 = in0

    return out0
