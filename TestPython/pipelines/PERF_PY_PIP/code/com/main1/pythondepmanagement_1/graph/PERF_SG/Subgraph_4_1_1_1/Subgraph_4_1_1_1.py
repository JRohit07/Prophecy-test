from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def Subgraph_4_1_1_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> DataFrame:
    Config.update(config)
    df_Script_2_1_1_1 = Script_2_1_1_1(spark, in0, in1, in2)
    df_Script_2_1_1_1 = collectMetrics(
        spark, 
        df_Script_2_1_1_1, 
        "Subgraph_4_1_1_1", 
        "zwiexzx-qUavHGqaE13BT$$EkNXFn-UnaZ7yv8PC86rQ", 
        "1ZXs1yod9bzdagZAusvHJ$$_IRmJkLDp616IATch06mt"
    )
    df_Subgraph_3_1_1_1 = Subgraph_3_1_1_1(spark, config.Subgraph_3_1_1_1, df_Script_2_1_1_1)

    return df_Subgraph_3_1_1_1
