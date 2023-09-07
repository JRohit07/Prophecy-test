from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_9_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_10_1_1 = Reformat_10_1_1(spark, in0)
    df_Reformat_10_1_1 = collectMetrics(
        spark, 
        df_Reformat_10_1_1, 
        "Subgraph_9_1_1", 
        "FqeSeDnclHLDathtszDif$$loaYXP1zILGBzDq5L5y7J", 
        "jZ4iY9nyv2Qwv9-W23GKI$$8NEyNZ-yQ5nIMIKzthgkj"
    )

    return df_Reformat_10_1_1
