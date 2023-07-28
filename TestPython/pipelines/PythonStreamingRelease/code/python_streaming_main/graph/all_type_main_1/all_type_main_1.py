from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def all_type_main_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    Config.update(config)
    df_Source_1_1_1 = Source_1_1_1(spark)
    Lookup_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = Reformat_1_1_1(spark, df_Source_1_1_1)
    df_Reformat_2_1_1 = Reformat_2_1_1(spark, in0)
    df_Join_1_1 = Join_1_1(spark, df_Reformat_1_1_1, df_Reformat_2_1_1)
    df_Limit_1_1_1 = Limit_1_1_1(spark, df_Join_1_1)
    df_Repartition_1_1_1 = Repartition_1_1_1(spark, df_Limit_1_1_1)
    df_RowDistributor_1_1_1_out0, df_RowDistributor_1_1_1_out1 = RowDistributor_1_1_1(spark, df_Repartition_1_1_1)
    df_Filter_1_1_1 = Filter_1_1_1(spark, df_Limit_1_1_1)
    df_OrderBy_1_1_1 = OrderBy_1_1_1(spark, df_Filter_1_1_1)
    df_OrderBy_3_1_1 = OrderBy_3_1_1(spark, in2)
    df_Deduplicate_3_1_1 = Deduplicate_3_1_1(spark, df_OrderBy_3_1_1)
    df_Aggregate_1_1_1 = Aggregate_1_1_1(spark, df_OrderBy_1_1_1)
    df_SchemaTransform_1_1_1 = SchemaTransform_1_1_1(spark, df_Aggregate_1_1_1)
    df_Deduplicate_1_1_1 = Deduplicate_1_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_2_1_1 = Deduplicate_2_1_1(spark, df_SchemaTransform_1_1_1)
    df_SetOperation_1_1_1 = SetOperation_1_1_1(spark, df_Deduplicate_1_1_1, df_Deduplicate_2_1_1)
    df_Reformat_5 = Reformat_5(spark, df_Reformat_2_1_1)
    df_WindowFunction_1_1_1 = WindowFunction_1_1_1(spark, df_SetOperation_1_1_1)
    df_Script_1_1_1 = Script_1_1_1(spark, df_WindowFunction_1_1_1)
    df_Subgraph_4_1_1 = Subgraph_4_1_1(
        spark, 
        config.Subgraph_4_1_1, 
        df_RowDistributor_1_1_1_out0, 
        df_RowDistributor_1_1_1_out1, 
        df_Script_1_1_1
    )
    df_Reformat_8_1_1 = Reformat_8_1_1(spark, in1)
    df_Limit_3_1_1 = Limit_3_1_1(spark, df_Reformat_8_1_1)
    df_Subgraph_1 = Subgraph_1(spark, config.Subgraph_1, df_Reformat_5)
    df_Subgraph_2 = Subgraph_2(spark, config.Subgraph_2, df_Subgraph_1)
    df_Reformat_4 = Reformat_4(spark, df_Source_1_1_1)
    py_sg_target_test_release(spark, df_Reformat_4)

    return df_Subgraph_4_1_1, df_Limit_3_1_1, df_Deduplicate_3_1_1
