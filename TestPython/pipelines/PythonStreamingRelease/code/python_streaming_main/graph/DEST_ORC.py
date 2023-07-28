from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DEST_ORC(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("orc")\
        .option("path", "dbfs:/tmp/streaming/target_release/orc/all_type_with_partition")\
        .option("checkpointLocation", "dbfs:/tmp/streaming/target_release/orc/checkpoint_all_type_with_partition")\
        .queryName("DEST_ORC_BtyzzWWfXGNZBcMyJPNM_$$_NfGWvDDhqQmtppLxHrW8")\
        .partitionBy("p_int", "p_float", "p_string")\
        .start()
