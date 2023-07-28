from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythongenericuse.config.ConfigStore import *
from pythongenericuse.udfs.UDFs import *
from prophecy.utils import *
from pythongenericuse.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_delta_all_type_no_partition = src_delta_all_type_no_partition(spark)
    df_Reformat_1 = Reformat_1(spark, df_src_delta_all_type_no_partition)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("s1", "test1")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PythonGenericUse")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PythonGenericUse")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
