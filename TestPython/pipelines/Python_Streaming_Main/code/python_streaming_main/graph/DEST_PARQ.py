from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DEST_PARQ(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("parquet")\
        .option("path", "dbfs:/tmp/streaming/target_release/parquet/all_type_with_partition")\
        .option("checkpointLocation", "dbfs:/tmp/streaming/target_release/parquet/checkpoint_all_type_with_partition")\
        .queryName("StreamingTarget_1_dslLapQGEmXqCS4S53W-y$$DMfT3uFAT_N7tZuW4GXo_")\
        .outputMode("append")\
        .partitionBy("p_int", "p_float", "p_string")\
        .start()
