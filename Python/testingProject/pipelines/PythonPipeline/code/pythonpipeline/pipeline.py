from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pythonpipeline.config.ConfigStore import *
from pythonpipeline.udfs.UDFs import *
from prophecy.utils import *
from pythonpipeline.graph import *

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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PythonPipeline")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PythonPipeline", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PythonPipeline")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
