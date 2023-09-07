from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *
from prophecy.utils import *
from pythonorganization.donot.openme12.graph import *

def pipeline(spark: SparkSession) -> None:
    df_all_type_part_parquet = all_type_part_parquet(spark)
    df_RowDistributor_1_out0, df_RowDistributor_1_out1, df_RowDistributor_1_out2, df_RowDistributor_1_out3 = RowDistributor_1(
        spark, 
        df_all_type_part_parquet
    )
    Lookup_1(spark, df_RowDistributor_1_out1)
    df_csv_special_chars = csv_special_chars(spark)
    df_Limit_1 = Limit_1(spark, df_csv_special_chars)
    df_Filter_1 = Filter_1(spark, df_Limit_1)
    df_ConfigAndUDF = ConfigAndUDF(spark, df_Filter_1)
    df_OrderBy_1 = OrderBy_1(spark, df_ConfigAndUDF)
    df_Deduplicate_1 = Deduplicate_1(spark, df_OrderBy_1)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_Deduplicate_1)
    df_SetOperation_1 = SetOperation_1(spark, df_SchemaTransform_1, df_SchemaTransform_1)
    df_delta = delta(spark)
    df_Limit_4 = Limit_4(spark, df_delta)
    df_Join_1 = Join_1(spark, df_all_type_part_parquet, df_all_type_part_parquet)
    df_Limit_7 = Limit_7(spark, df_Join_1)
    df_Repartition_1 = Repartition_1(spark, df_Limit_7)
    df_SubGraph_2 = SubGraph_2(spark, Config.SubGraph_2, df_Repartition_1, df_RowDistributor_1_out0)
    df_Limit_8 = Limit_8(spark, df_SubGraph_2)
    df_Reformat_6 = Reformat_6(spark, df_Limit_8)
    df_orc_src = orc_src(spark)
    df_Deduplicate_2 = Deduplicate_2(spark, df_orc_src)
    df_Reformat_5 = Reformat_5(spark, df_Deduplicate_2)
    df_Join_3 = Join_3(spark, df_Reformat_6, df_Reformat_5)
    df_avro = avro(spark)
    df_OrderBy_3 = OrderBy_3(spark, df_avro)
    df_Reformat_7 = Reformat_7(spark, df_OrderBy_3)
    df_Join_4 = Join_4(spark, df_Join_3, df_Reformat_7)
    df_csv_all_type = csv_all_type(spark)
    df_Aggregate_1 = Aggregate_1(spark, df_SetOperation_1)
    df_text = text(spark)
    df_Reformat_4 = Reformat_4(spark, df_text)
    df_all_type_main_1_out0, df_all_type_main_1_out1, df_all_type_main_1_out2 = all_type_main_1(
        spark, 
        Config.all_type_main_1, 
        df_all_type_part_parquet, 
        df_all_type_part_parquet, 
        df_all_type_part_parquet
    )
    df_Script_1 = Script_1(spark, df_Aggregate_1)
    df_json_in = json_in(spark)
    df_Reformat_16 = Reformat_16(spark, df_json_in)
    df_catalog = catalog(spark)
    df_src_jdbc_userandpass_test_table = src_jdbc_userandpass_test_table(spark)
    df_Reformat_9 = Reformat_9(spark, df_RowDistributor_1_out2)
    df_Reformat_15 = Reformat_15(spark, df_csv_all_type)
    df_OrderBy_4 = OrderBy_4(spark, df_delta)
    df_Limit_6 = Limit_6(spark, df_catalog)
    df_Script_3 = Script_3(
        spark, 
        df_Limit_6, 
        df_Limit_6, 
        df_OrderBy_4, 
        df_Limit_4, 
        df_Reformat_16, 
        df_Reformat_15, 
        df_OrderBy_1
    )
    df_Script_6 = Script_6(
        spark, 
        df_all_type_main_1_out0, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out2, 
        df_all_type_main_1_out2, 
        df_all_type_main_1_out2
    )
    df_Reformat_11 = Reformat_11(spark, df_Script_6)
    df_Limit_3 = Limit_3(spark, df_Script_1)
    df_SubGraph_7 = SubGraph_7(spark, Config.SubGraph_7, df_Script_3)
    df_Limit_2 = Limit_2(spark, df_SubGraph_7)
    df_src_parquet_all_type_no_partition = src_parquet_all_type_no_partition(spark)
    df_Limit_9 = Limit_9(spark, df_Join_4)
    df_WindowFunction_1 = WindowFunction_1(spark, df_RowDistributor_1_out3)
    Script_2(spark, df_WindowFunction_1)
    df_ComplexExpr = ComplexExpr(spark, df_src_parquet_all_type_no_partition)
    df_OrderBy_5 = OrderBy_5(spark, df_ComplexExpr)
    df_Limit_10 = Limit_10(spark, df_OrderBy_5)
    df_Join_5 = Join_5(spark, df_Limit_9, df_Reformat_4)
    df_Reformat_10 = Reformat_10(spark, df_src_jdbc_userandpass_test_table)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("spark_config1", "spark_config1 value")
    spark.conf.set("spark_config2", "spark_config2 value")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/DONOT_OPEN_PYTHON")
    spark.sparkContext._jsc.hadoopConfiguration().set("hadoop_config1", "hadoop_config1 value")
    spark.sparkContext._jsc.hadoopConfiguration().set("hadoop_config2", "hadoop_config2 value")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/DONOT_OPEN_PYTHON")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
