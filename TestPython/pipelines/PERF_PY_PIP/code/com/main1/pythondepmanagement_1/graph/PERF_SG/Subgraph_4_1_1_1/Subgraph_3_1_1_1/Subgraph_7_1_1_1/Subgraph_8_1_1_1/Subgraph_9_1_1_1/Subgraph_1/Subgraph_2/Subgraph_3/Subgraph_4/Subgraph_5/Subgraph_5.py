from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from . import *
from .config import *

def Subgraph_5(spark: SparkSession, config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(config)
    df_Reformat_3 = Reformat_3(spark, in0)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "Subgraph_5", 
        "ALI0n8ySRdOUBMI-sulKa$$Kc9uRzy-waSzBIFdeafG_", 
        "Ict-FIwvw4x4vFe_9f8DG$$xEhgauI4RRJXignmwIU3y"
    )

    return df_Reformat_3
