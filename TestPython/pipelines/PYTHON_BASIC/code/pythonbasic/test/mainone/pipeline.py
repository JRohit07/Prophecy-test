from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *
from prophecy.utils import *
from pythonbasic.test.mainone.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_avro_CustsDatasetInput_1 = src_avro_CustsDatasetInput_1(spark)
    Lookup_1(spark, df_src_avro_CustsDatasetInput_1)
    df_src_avro_CustsDatasetInput = src_avro_CustsDatasetInput(spark)
    df_Limit_1 = Limit_1(spark, df_src_avro_CustsDatasetInput)

    if (Config.c_int < - 100):
        df_PassthisBuddy = PassthisBuddy(spark, df_Limit_1)
        df_PassthisBuddy = df_PassthisBuddy.cache()
    else:
        df_PassthisBuddy = df_Limit_1

    df_Deduplicate_1 = Deduplicate_1(spark, df_PassthisBuddy)
    df_UL_Reformat_4 = UL_Reformat_4(spark, df_src_avro_CustsDatasetInput)
    df_UL_Reformat_4 = df_UL_Reformat_4.cache()

    if not Config.c_int > - 100:
        df_UL_Join_1 = UL_Join_1(spark, df_UL_Reformat_4, df_UL_Reformat_4)
        df_UL_Join_1 = df_UL_Join_1.cache()
        df_UL_OrderBy_1 = UL_OrderBy_1(spark, df_UL_Join_1)
        dest_testpythonsanitybasic(spark, df_UL_OrderBy_1)

    if not Config.c_int > - 100:

        if (Config.c_int > - 100):
            df_SchemaTransform_1 = SchemaTransform_1(spark, df_src_avro_CustsDatasetInput)
        else:
            df_SchemaTransform_1 = df_src_avro_CustsDatasetInput

        df_Reformat_4 = Reformat_4(spark, df_SchemaTransform_1)
    else:
        df_Reformat_4 = None

    if not Config.c_int > - 100:
        df_Reformat_3 = Reformat_3(spark, df_SchemaTransform_1)
    else:
        df_Reformat_3 = None

    if not Config.c_int > - 100:

        if (Config.c_int > - 100):
            df_UL_Aggregate_1 = UL_Aggregate_1(spark, df_src_avro_CustsDatasetInput)
            df_UL_Aggregate_1 = df_UL_Aggregate_1.cache()
        else:
            df_UL_Aggregate_1 = df_src_avro_CustsDatasetInput

        df_Reformat_1 = Reformat_1(spark, df_UL_Aggregate_1)
    else:
        df_Reformat_1 = None

    df_Script_1 = Script_1(spark, df_src_avro_CustsDatasetInput)
    df_Script_1 = df_Script_1.cache()
    df_DONOT_DELETE = DONOT_DELETE(spark, df_src_avro_CustsDatasetInput)

    if not Config.c_int < - 100:

        if (Config.c_int < - 100):
            df_Removethisbuddy = Removethisbuddy(spark, df_Limit_1)
            df_Removethisbuddy = df_Removethisbuddy.cache()
        else:
            df_Removethisbuddy = df_Limit_1

        df_Deduplicate_1_1 = Deduplicate_1_1(spark, df_Removethisbuddy)
    else:
        df_Deduplicate_1_1 = None

    if not ((Config.c_int > - 100) and (Config.c_int > - 100)):
        df_CompareColumns_1 = CompareColumns_1(spark, df_SchemaTransform_1, df_Reformat_4)
    else:
        df_CompareColumns_1 = None

    df_Subgraph_1 = Subgraph_1(spark, Config.Subgraph_1, df_src_avro_CustsDatasetInput)
    df_Subgraph_1 = df_Subgraph_1.cache()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("spark.sql.optimizer.excludedRules", "org.apache.spark.sql.catalyst.optimizer.ColumnPruning")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_BASIC")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_BASIC", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_BASIC")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
