from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from emr_synapse.config.ConfigStore import *
from emr_synapse.udfs.UDFs import *
from prophecy.utils import *
from emr_synapse.graph import *

def pipeline(spark: SparkSession) -> None:
    df_mydataset = mydataset(spark)
    df_Reformat_1 = Reformat_1(spark, df_mydataset)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/EMR_Synapse")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/EMR_Synapse", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/EMR_Synapse")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
