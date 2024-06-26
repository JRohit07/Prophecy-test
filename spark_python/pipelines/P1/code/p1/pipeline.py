from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from p1.config.ConfigStore import *
from p1.udfs.UDFs import *
from prophecy.utils import *
from p1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_annual_data = annual_data(spark)
    df_Reformat_1 = Reformat_1(spark, df_annual_data)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/P1")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/P1", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/P1")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
