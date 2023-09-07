from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_3_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_9_1_1 = Reformat_9_1_1(spark, in0)
    df_Reformat_9_1_1 = collectMetrics(
        spark, 
        df_Reformat_9_1_1, 
        "Subgraph_3_1_1", 
        "1eDyEEg0DYJ9sSvXa5k6y$$lNTfjbHgymr5JPyVO_VLs", 
        "jbC8bVGEnnlGcNfStEXGJ$$aiDOfZ_tdqk13YmKe0te8"
    )
    df_Subgraph_7_1_1 = Subgraph_7_1_1(spark, config.Subgraph_7_1_1, df_Reformat_9_1_1)

    return df_Subgraph_7_1_1
