from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *
from prophecy.utils import *
from pythonbasic.test.mainone.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_special_char_column_name = src_csv_special_char_column_name(spark)

    if not Config.c_int > 0:

        if (Config.c_int > 0):
            df_Reformat_1 = Reformat_1(spark, df_src_csv_special_char_column_name)
            df_Reformat_1 = df_Reformat_1.cache()
        else:
            df_Reformat_1 = df_src_csv_special_char_column_name

        dest_csv_py_io_only(spark, df_Reformat_1)

    if not Config.c_int > 0:
        df_Script_4 = Script_4(spark, df_Reformat_1)
    else:
        df_Script_4 = None

    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_src_csv_special_char_column_name)

    if not Config.c_int < 0:
        df_Removal = Removal(spark, df_RowDistributor_1_out1)
        df_Filter_1 = Filter_1(spark, df_Removal)
    else:
        df_Filter_1 = None

    df_Script_5 = Script_5(spark, df_src_csv_special_char_column_name)
    df_Script_5 = df_Script_5.cache()
    df_Reformat_3 = Reformat_3(spark, df_Script_5)
    df_Join_1 = Join_1(spark, df_RowDistributor_1_out0, df_RowDistributor_1_out1)
    df_Join_1 = df_Join_1.cache()

    if (Config.c_int < 0):
        df_Passthrough = Passthrough(spark, df_Join_1)
        df_Passthrough = df_Passthrough.cache()
    else:
        df_Passthrough = df_Join_1

    df_Filter_1_1 = Filter_1_1(spark, df_Passthrough)
    df_Filter_1_1 = df_Filter_1_1.cache()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/EM_DISABLED_PYTHON_BASIC")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/EM_DISABLED_PYTHON_BASIC", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/EM_DISABLED_PYTHON_BASIC")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
