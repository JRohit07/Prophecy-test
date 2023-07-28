from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *
from prophecy.utils import *
from python_streaming_main.graph import *

def pipeline(spark: SparkSession) -> None:
    df_QA_KAFKA = QA_KAFKA(spark)
    df_FlattenSchema_2_1 = FlattenSchema_2_1(spark, df_QA_KAFKA)
    df_Watermark_2 = Watermark_2(spark, df_FlattenSchema_2_1)
    df_Parquet_Standard = Parquet_Standard(spark)
    df_ORC_ST = ORC_ST(spark)
    df_SQLStatement_1 = SQLStatement_1(spark, df_ORC_ST)
    df_Script_1 = Script_1(spark, df_SQLStatement_1)
    df_Deduplicate_1 = Deduplicate_1(spark, df_Parquet_Standard)
    df_Filter_1 = Filter_1(spark, df_Deduplicate_1)
    df_src_parquet_all_type_and_partition_withspacehyphens_renamed = src_parquet_all_type_and_partition_withspacehyphens_renamed(
        spark
    )
    DEST_ORC(spark, df_Script_1)
    df_SQS_PARQUET = SQS_PARQUET(spark)
    df_Reformat_2 = Reformat_2(spark, df_SQS_PARQUET)
    SPLUNK_DEST(spark, df_Reformat_2)
    df_all_type_main_1_out0, df_all_type_main_1_out1, df_all_type_main_1_out2 = all_type_main_1(
        spark, 
        Config.all_type_main_1, 
        df_src_parquet_all_type_and_partition_withspacehyphens_renamed, 
        df_src_parquet_all_type_and_partition_withspacehyphens_renamed, 
        df_src_parquet_all_type_and_partition_withspacehyphens_renamed
    )
    df_SetOperation_1 = SetOperation_1(spark, df_Filter_1, df_Filter_1)
    df_DELTA_SRC = DELTA_SRC(spark)
    df_Reformat_1 = Reformat_1(spark, df_DELTA_SRC)
    DELTA_DEST(spark, df_Reformat_1)
    df_Aggregate_1_1 = Aggregate_1_1(spark, df_Watermark_2)
    QA_KAFKA_Dest(spark, df_Aggregate_1_1)
    df_DEV_KAFKA = DEV_KAFKA(spark)
    df_FlattenSchema_2 = FlattenSchema_2(spark, df_DEV_KAFKA)
    df_Watermark_1 = Watermark_1(spark, df_FlattenSchema_2)
    df_CSV_AL = CSV_AL(spark)
    df_Subgraph_1 = Subgraph_1(spark, Config.Subgraph_1, df_CSV_AL)
    DEST_CSV(spark, df_Subgraph_1)
    df_Aggregate_1 = Aggregate_1(spark, df_Watermark_1)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_SetOperation_1)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_SchemaTransform_1)
    DEST_PARQ(spark, df_FlattenSchema_1)
    df_JSON_SRC = JSON_SRC(spark)
    df_Filter_2 = Filter_2(spark, df_JSON_SRC)
    JSON_DEST(spark, df_Filter_2)
    DEST_KAFKA(spark, df_Aggregate_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Python_Streaming_Main")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Python_Streaming_Main", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Python_Streaming_Main")

    pipeline(spark)
    
    spark.streams.resetTerminated()
    spark.streams.awaitAnyTermination()
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
