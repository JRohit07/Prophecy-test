from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def dummy_snowflake(spark: SparkSession, in0: DataFrame):
    from pyspark.dbutils import DBUtils
    options = {
        "sfUrl": "test",
        "sfUser": "test",
        "sfPassword": "test",
        "sfDatabase": "",
        "sfSchema": "",
        "sfWarehouse": ""
    }
    writer = in0.write.format("snowflake").options(**options)
    writer.option("dbtable", "test").mode("overwrite").save()
