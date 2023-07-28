from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def SQLStatement_1(spark: SparkSession, in0: DataFrame, input1: DataFrame) -> (DataFrame, DataFrame, DataFrame):

    try:
        registerUDFs(spark)
    except NameError:
        print("registerUDFs not working")

    in0.createOrReplaceTempView("in0")
    input1.createOrReplaceTempView("input1")
    df1 = spark.sql("select * from in0 where in0.`c  - int` > '$c_0' and in0.`c- short` > 1")
    df2 = spark.sql("select * from in0 where in0.`c  - int` != '$c_int' and in0.`c-string` not like '$c_sql_pattern'")
    df3 = spark.sql(
        "SELECT `c- short`, `c  - int`, `c-string`,\n       case when `c-string`='NY' then 'New York'\n            when `c-string`='CA' then 'California'\n            when `c-string`='FL' then 'Florida'\n            else 'Other' end as state,\n       `c  - int` + 5 as age_plus_5,\n       concat(`c- short`, ' ', c_double) as full_name\nFROM input1\nWHERE p_string like '%a%'\nORDER BY `c-string` DESC"
    )

    return df1, df2, df3
