from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from com.sg_src.main.config.ConfigStore import *
from com.sg_src.main.udfs.UDFs import *
from prophecy.utils import *
from com.sg_src.main.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_parquet_all_type_and_partition_withspacehyphens = src_parquet_all_type_and_partition_withspacehyphens(spark)
    df_all_type_main_pythonsg_out0, df_all_type_main_pythonsg_out1, df_all_type_main_pythonsg_out2 = all_type_main_pythonsg(
        spark, 
        Config.all_type_main_pythonsg, 
        df_src_parquet_all_type_and_partition_withspacehyphens, 
        df_src_parquet_all_type_and_partition_withspacehyphens, 
        df_src_parquet_all_type_and_partition_withspacehyphens
    )
    df_Reformat_1 = Reformat_1(spark, df_src_parquet_all_type_and_partition_withspacehyphens)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_SG_SRC")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_SG_SRC", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_SG_SRC")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
