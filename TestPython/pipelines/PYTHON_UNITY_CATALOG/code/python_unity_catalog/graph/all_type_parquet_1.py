from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_unity_catalog.config.ConfigStore import *
from python_unity_catalog.udfs.UDFs import *

def all_type_parquet_1(spark: SparkSession) -> DataFrame:
    return spark.read.table(f"`qa_database`.`all_type_parquet`")
