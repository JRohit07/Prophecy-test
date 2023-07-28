from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Filter_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        (
          (col("`c   short  --`") > lit(Config.c_0))
          & (~ col("`c-int-column type`").like(Config.c_regex1) & ~ col("`c___-- string`").like(Config.c_regex2))
        )
    )
