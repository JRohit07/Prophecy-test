from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DELTA_SRC(spark: SparkSession) -> DataFrame:
    return spark.readStream.format("delta").load("dbfs:/Prophecy/qa_data/streaming/delta/all_type_with_partition")
