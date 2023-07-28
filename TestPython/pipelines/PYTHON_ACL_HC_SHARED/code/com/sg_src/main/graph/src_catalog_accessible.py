from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from com.sg_src.main.config.ConfigStore import *
from com.sg_src.main.udfs.UDFs import *

def src_catalog_accessible(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"qa_database_acl.table_with_read_permission_for_user")
