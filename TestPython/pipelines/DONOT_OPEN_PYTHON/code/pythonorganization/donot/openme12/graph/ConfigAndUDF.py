from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythonorganization.donot.openme12.config.ConfigStore import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def ConfigAndUDF(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("`c   short  --`"), 
        col("`c-int-column type`"), 
        col("`-- c-long`"), 
        col("`c-decimal`"), 
        col("`c  float`"), 
        col("`c--boolean`"), 
        col("`c- - -double`"), 
        col("`c___-- string`"), 
        col("`c  date`"), 
        col("c_timestamp"), 
        squared(col("`c   short  --`")).alias("squared_short"), 
        factorial(col("`c   short  --`")).alias("factorial_short"), 
        random_string(lit(10), col("`c___-- string`")).alias("random_string_value"), 
        concat(
            col("`c  date`"), 
            lit(Config.CONFIG_DB_SECRETS), 
            lit(Config.CONFIG_STR), 
            lit(Config.CONFIG_BOOLEAN), 
            lit(Config.CONFIG_DOUBLE), 
            lit(Config.CONFIG_INT), 
            lit(Config.CONFIG_FLOAT), 
            lit(Config.CONFIG_SHORT)
          )\
          .alias("config_values"), 
        udf_scipy_dependency().alias("udf_scipy_dependency")
    )
