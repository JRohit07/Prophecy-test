from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythongenericuse.config.ConfigStore import *
from pythongenericuse.udfs.UDFs import *

def src_delta_all_type_no_partition(spark: SparkSession) -> DataFrame:
    return spark.read.format("delta").load("dbfs:/Prophecy/qa_data/delta/all_type_no_partition")
