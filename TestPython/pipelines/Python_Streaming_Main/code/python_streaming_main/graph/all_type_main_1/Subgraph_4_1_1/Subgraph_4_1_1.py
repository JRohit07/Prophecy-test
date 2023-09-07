from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_4_1_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> DataFrame:
    Config.update(config)
    df_Script_2_1_1 = Script_2_1_1(spark, in0, in1, in2)
    df_Subgraph_3_1_1 = Subgraph_3_1_1(spark, config.Subgraph_3_1_1, df_Script_2_1_1)
    df_very_complex_source = very_complex_source(spark)
    df_Reformat_2 = Reformat_2(spark, df_Script_2_1_1)
    df_Reformat_7 = Reformat_7(spark, df_very_complex_source)
    df_Reformat_8 = Reformat_8(spark, df_Reformat_7)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_very_complex_source)
    df_Reformat_6 = Reformat_6(spark, df_FlattenSchema_1)

    return df_Subgraph_3_1_1
