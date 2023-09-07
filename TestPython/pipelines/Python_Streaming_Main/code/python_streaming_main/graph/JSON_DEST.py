from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def JSON_DEST(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("json")\
        .option("path", "dbfs:/tmp/streaming/target_release/json/all_type_with_partition")\
        .option("checkpointLocation", "dbfs:/tmp/streaming/target_release/json/checkpoint_all_type_with_partition")\
        .queryName("JSON_DEST_5n7jWSD3Tg66A4kDm3DnQ$$pT3unTr2J4TQJaavPsGEn")\
        .outputMode("append")\
        .partitionBy("p_int", "p_float", "p_string")\
        .trigger(processingTime = "2 minutes")\
        .start()
