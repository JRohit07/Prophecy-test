from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from perf_unitest_generate.config.ConfigStore import *
from perf_unitest_generate.udfs.UDFs import *
from prophecy.utils import *
from perf_unitest_generate.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_json_input_custs = src_json_input_custs(spark)
    Lookup_1(spark, df_src_json_input_custs)
    df_Reformat_1 = Reformat_1(spark, df_src_json_input_custs)
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    df_SetOperation_1 = SetOperation_1(spark, df_OrderBy_1, df_OrderBy_1)
    df_Deduplicate_1 = Deduplicate_1(spark, df_SetOperation_1)
    df_Join_1 = Join_1(spark, df_Deduplicate_1, df_Deduplicate_1)
    df_Subgraph_1 = Subgraph_1(spark, df_Join_1)
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_src_json_input_custs)
    df_WindowFunction_1 = WindowFunction_1(spark, df_SchemaTransform_1)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_src_json_input_custs)
    df_Aggregate_1 = Aggregate_1(spark, df_SchemaTransform_1)
    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_OrderBy_1)
    df_Limit_1 = Limit_1(spark, df_RowDistributor_1_out0)
    df_Repartition_1 = Repartition_1(spark, df_RowDistributor_1_out1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PERF_UNITEST_GENERATE")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PERF_UNITEST_GENERATE")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
