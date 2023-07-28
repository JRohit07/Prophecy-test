from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def table_with_read_permission_for_user_1(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"qa_database_acl.table_with_read_permission_for_user")
