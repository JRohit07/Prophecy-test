from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def Subgraph_8_1_1_1(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Subgraph_9_1_1_1 = Subgraph_9_1_1_1(spark, config.Subgraph_9_1_1_1, in0)

    return df_Subgraph_9_1_1_1
