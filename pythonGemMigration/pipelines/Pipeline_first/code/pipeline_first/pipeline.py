from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *
from prophecy.utils import *
from pipeline_first.graph import *

def pipeline(spark: SparkSession) -> None:
    df_source_5 = source_5(spark)
    df_source_2 = source_2(spark)
    target_2(spark, df_source_2)
    df_source_1 = source_1(spark)
    target_1(spark, df_source_1)
    df_source_7 = source_7(spark)
    target_7(spark, df_source_7)
    df_source_4 = source_4(spark)
    target_4(spark, df_source_4)
    df_source_8 = source_8(spark)
    target_8(spark, df_source_8)
    target_5(spark, df_source_5)
    df_source_6 = source_6(spark)
    df_source_3 = source_3(spark)
    target_3(spark, df_source_3)
    df_source_9 = source_9(spark)
    target_9(spark, df_source_9)
    target_6(spark, df_source_6)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline_first")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline_first", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline_first")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
