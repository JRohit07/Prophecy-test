from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from p12.config.ConfigStore import *
from p12.udfs.UDFs import *
from prophecy.utils import *
from p12.graph import *

def pipeline(spark: SparkSession) -> None:
    pass

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/P12")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/P12", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/P12")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
