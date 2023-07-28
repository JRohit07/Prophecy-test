from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def SQLStatement_1(spark: SparkSession, in0: DataFrame) -> (DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    in0.createOrReplaceTempView("in0")
    df1 = spark.sql("select c_tinyint,c_smallint,p_int,p_float,p_string from in0")

    return df1
