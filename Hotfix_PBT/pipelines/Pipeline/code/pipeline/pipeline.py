from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline.config.ConfigStore import *
from pipeline.udfs.UDFs import *
from prophecy.utils import *
from pipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_test_uc_seed_1 = test_uc_seed_1(spark)
    df_Reformat_1 = Reformat_1(spark, df_test_uc_seed_1)
    df_Limit_1 = Limit_1(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Pipeline")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/Pipeline")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
