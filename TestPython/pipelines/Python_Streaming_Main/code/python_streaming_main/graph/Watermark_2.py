from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def Watermark_2(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.withWatermark("timestamp", "10 minutes")
