from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DELTA_DEST(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("delta")\
        .option("checkpointLocation", "dbfs:/tmp/streaming/target_release/delta/checkpoint_all_type_with_partition/")\
        .queryName("StreamingTarget_2_p7Z47OqYK_gkBH_Q1Qf7G$$XvSjKKLfsyQNvUD8FWe1T")\
        .outputMode("append")\
        .start("dbfs:/tmp/streaming/target_release/delta/all_type_with_partition/")
