from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DEST_CSV(spark: SparkSession, in0: DataFrame):
    in0.writeStream\
        .format("csv")\
        .option("checkpointLocation", "dbfs:/tmp/streaming/target_release/csv/checkpoint_all_type_with_partition")\
        .queryName("DEST_CSV_dyS-2nCTytvNN5TyN12Ex$$8m2smb5dv03ZDuXeECfA7")\
        .option("header", True)\
        .option("sep", ",")\
        .option("ignoreLeadingWhiteSpace", True)\
        .option("ignoreTrailingWhiteSpace", True)\
        .outputMode("append")\
        .partitionBy("p_int", "p_float", "p_string")\
        .option("path", "dbfs:/tmp/streaming/target_release/csv/all_type_with_partition")\
        .start()
