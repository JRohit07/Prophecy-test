from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from pythonbasic.test.mainone.udfs.UDFs import *

def UL_Join_1_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.customer_id") == col("in1.customer_id")), "inner")\
        .select(lookup("TestLookup", col("in0.customer_id"), col("in1.email"))\
        .getField("first_name")\
        .alias("c_lookup_first_name"), lookup("TestLookup", col("in0.customer_id"), col("in1.email"))\
        .getField("last_name")\
        .alias("c_lookup_last_name"), col("in0.customer_id").alias("customer_id"), concat(col("in0.first_name"), lookup("TestLookup", col("in0.customer_id"), col("in1.email")).getField("last_name"))\
        .alias("first_name"), col("in0.last_name").alias("last_name"), col("in0.phone").alias("phone"), col("in0.email").alias("email"), col("in0.country_code").alias("country_code"), col("in0.account_open_date").alias("account_open_date"), col("in0.account_flags").alias("account_flags"))
