from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipfirst.config.ConfigStore import *
from pipfirst.functions import *
from prophecy.utils import *
from pipfirst.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset = dataset(spark)
    df_Filter_1 = Filter_1(spark, df_dataset)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("PipFirst")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PipFirst")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/PipFirst", config = Config)(pipeline)

if __name__ == "__main__":
    main()
