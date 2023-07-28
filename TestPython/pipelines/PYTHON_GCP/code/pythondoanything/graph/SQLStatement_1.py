from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def SQLStatement_1(spark: SparkSession, in0: DataFrame) -> (DataFrame, DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    in0.createOrReplaceTempView("in0")
    df1 = spark.sql("select * from in0 where in0.`c  - int` > 0 and in0.`c- short` > 1")
    df2 = spark.sql("select * from in0 where in0.`c  - int` != '$c_int' and in0.`c-string` not like '$c_sql_pattern'")

    return df1, df2
