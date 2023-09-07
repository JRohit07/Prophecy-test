from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SubGraph_2(spark: SparkSession, config: SubgraphConfig, in0: DataFrame, in1: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_1 = Reformat_1(spark, in1)
    df_Script_5 = Script_5(spark, df_Reformat_1)
    df_Filter_4 = Filter_4(spark, df_Script_5)
    df_Reformat_2 = Reformat_2(spark, in0)
    df_Filter_2 = Filter_2(spark, df_Reformat_2)
    df_SubGraph_3 = SubGraph_3(spark, config.SubGraph_3, df_Filter_2)

    return df_SubGraph_3
