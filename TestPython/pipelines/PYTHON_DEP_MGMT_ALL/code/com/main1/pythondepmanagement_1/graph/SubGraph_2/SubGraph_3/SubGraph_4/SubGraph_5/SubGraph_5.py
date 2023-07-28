from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def SubGraph_5(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_OrderBy_2 = OrderBy_2(spark, in0)
    df_OrderBy_2 = collectMetrics(
        spark, 
        df_OrderBy_2, 
        "SubGraph_5", 
        "3lHssRL8kBVfhwz5lBAzs$$vxVLkeHHIWCgwotbBrmB6", 
        "KATyXv5cFGLVSgtDWIJbv$$GvWy7dDFldvYYW6o517YA"
    )
    df_SubGraph_6 = SubGraph_6(spark, config.SubGraph_6, df_OrderBy_2)

    return df_SubGraph_6
