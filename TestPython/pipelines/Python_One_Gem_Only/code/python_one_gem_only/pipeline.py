from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from python_one_gem_only.config.ConfigStore import *
from python_one_gem_only.udfs.UDFs import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from python_one_gem_only.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_parquet_all_type_no_partition = src_parquet_all_type_no_partition(spark)
    df_Reformat_1 = Reformat_1(spark, df_src_parquet_all_type_no_partition)
    df_Reformat_2 = Reformat_2(spark, df_Reformat_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/Python_One_Gem_Only")
    registerUDFs(spark)
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/Python_One_Gem_Only")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
