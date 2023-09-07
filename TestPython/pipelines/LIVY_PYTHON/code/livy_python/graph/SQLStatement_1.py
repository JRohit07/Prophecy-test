from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from livy_python.config.ConfigStore import *
from livy_python.udfs.UDFs import *

def SQLStatement_1(
        spark: SparkSession,
        input_0: DataFrame, 
        in1: DataFrame, 
        in2: DataFrame
) -> (DataFrame, DataFrame, DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    input_0.createOrReplaceTempView("input_0")
    in1.createOrReplaceTempView("in1")
    in2.createOrReplaceTempView("in2")
    df1 = spark.sql(
        "select input_0.year,input_0.variable,in1.value,input_0.unit,input_0.c_config from input_0,in1 where input_0.industry_code_ANZSIC=in1.industry_code_ANZSIC"
    )
    df2 = spark.sql("select * from in1 where industry_code_ANZSIC like '%A%'")
    df3 = spark.sql("select * from in2 where variable like '%Total%'")

    return df1, df2, df3
