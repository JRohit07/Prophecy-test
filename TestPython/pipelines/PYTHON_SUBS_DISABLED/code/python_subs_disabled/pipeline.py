from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *
from prophecy.utils import *
from python_subs_disabled.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_delta_all_type_no_partition_renamed = src_delta_all_type_no_partition_renamed(spark)
    dummy_snowflake(spark, df_src_delta_all_type_no_partition_renamed)
    df_create_data_1 = create_data_1(spark)
    df_data_from_api = data_from_api(spark, df_create_data_1)
    df_parse = parse(spark, df_data_from_api)
    df_filter_1 = filter_1(spark, df_parse)
    df_create_data = create_data(spark)
    df_reformat_url = reformat_url(spark, df_create_data)
    df_rate_from_api = rate_from_api(spark, df_reformat_url)
    dummy_redshift_dest(spark, df_src_delta_all_type_no_partition_renamed)
    dummy_dest_delta_merge_scd(spark, df_src_delta_all_type_no_partition_renamed)
    dummy_catalog_delta_merge_scd(spark, df_src_delta_all_type_no_partition_renamed)
    dummy_catalog_delta(spark, df_src_delta_all_type_no_partition_renamed)
    df_parse_data = parse_data(spark, df_rate_from_api)
    df_filter_2 = filter_2(spark, df_parse_data)
    dummy_delta_merge(spark, df_src_delta_all_type_no_partition_renamed)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_SUBS_DISABLED")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_SUBS_DISABLED")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
