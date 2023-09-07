from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    import sys
    sys.stdout.write("Hello Standard Output!\n")
    sys.stderr.write("Hello Standard Error!\n")
    print("Hello Standard Output!")
    print("Hello Standard Error!", file = sys.stderr)
    out0 = in0

    return out0
