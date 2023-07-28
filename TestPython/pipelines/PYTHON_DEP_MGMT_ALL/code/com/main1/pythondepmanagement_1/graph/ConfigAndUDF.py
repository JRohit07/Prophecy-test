from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

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
            lit(Config.c_config_38), 
            lit(Config.CONFIG_DB_SECRETS), 
            lit(Config.CONFIG_STR), 
            lit(Config.CONFIG_BOOLEAN), 
            lit(Config.CONFIG_DOUBLE), 
            lit(Config.CONFIG_INT), 
            lit(Config.CONFIG_FLOAT), 
            lit(Config.CONFIG_SHORT)
          )\
          .alias("config_values"), 
        udf_scipy_dependency().alias("udf_scipy_dependency"), 
        concat(lit(Config.c_str), col("`c  date`")).alias("c_config_str"), 
        concat(lit(Config.c_record_complex.cr_array_int[0]), lit(Config.c_array_complex[0].car_record.carr_array_int[0]))\
          .alias("c_complex_string")
    )
