from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def Subgraph_7_1_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_2 = Reformat_2(spark, in0)
    df_Reformat_2 = collectMetrics(
        spark, 
        df_Reformat_2, 
        "Subgraph_7_1_1_1", 
        "WWkocOfAi3M1rAKTGbAiz$$qg6pc77QaoXjmRp5Ij8tw", 
        "vFrC6wmO9D9P4793q7qaI$$1S79MXT7VRdepWjDsWcOx"
    )
    df_Subgraph_8_1_1_1 = Subgraph_8_1_1_1(spark, config.Subgraph_8_1_1_1, df_Reformat_2)

    return df_Subgraph_8_1_1_1
