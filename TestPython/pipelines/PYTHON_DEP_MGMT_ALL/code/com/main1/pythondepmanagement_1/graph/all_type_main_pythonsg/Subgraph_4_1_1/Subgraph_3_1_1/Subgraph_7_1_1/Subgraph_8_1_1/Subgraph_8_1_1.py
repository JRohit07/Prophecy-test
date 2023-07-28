from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def Subgraph_8_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_OrderBy_5_1_1 = OrderBy_5_1_1(spark, in0)
    df_OrderBy_5_1_1 = collectMetrics(
        spark, 
        df_OrderBy_5_1_1, 
        "Subgraph_8_1_1", 
        "2OW_e2OWirNT8Iv2PeGCl$$SKDpfYhEYwrjhZGd0kyPt", 
        "JDJyA499iZD_5Wi2NBhj5$$M4X0Uc5xpdQ2e6kl5PB6_"
    )
    df_Subgraph_9_1_1 = Subgraph_9_1_1(spark, config.Subgraph_9_1_1, df_OrderBy_5_1_1)

    return df_Subgraph_9_1_1
