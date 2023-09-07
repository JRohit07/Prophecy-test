from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def src_delta_all_type_no_partition_renamed(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/Prophecy/qa_data/delta/all_type_no_partition")
