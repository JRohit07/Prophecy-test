from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def SchemaTransform_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out = in0\
              .withColumn("full_name", concat(col("first_name"), col("last_name")))\
              .drop("account_flags")\
              .drop("account_open_date")\
              .drop("phone")\
              .withColumnRenamed("email", "email_main")

    if "customer_id" not in in0.columns:
        out = in0\
                  .withColumn("full_name", concat(col("first_name"), col("last_name")))\
                  .drop("account_flags")\
                  .drop("account_open_date")\
                  .drop("phone")\
                  .withColumnRenamed("email", "email_main")\
                  .withColumn("customer_id", lit(10))

    return out
