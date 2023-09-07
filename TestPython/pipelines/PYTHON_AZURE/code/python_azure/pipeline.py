from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from python_azure.config.ConfigStore import *
from python_azure.udfs.UDFs import *
from prophecy.utils import *
from python_azure.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_azure = src_azure(spark)
    df_Reformat_1 = Reformat_1(spark, df_src_azure)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_AZURE")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_AZURE", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_AZURE")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
