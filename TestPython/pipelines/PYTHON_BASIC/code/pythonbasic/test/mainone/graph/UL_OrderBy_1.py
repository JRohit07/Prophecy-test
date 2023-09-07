from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *

def UL_OrderBy_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(
        concat(col("last_name"), lookup("TestLookup", col("customer_id"), col("email")).getField("first_name")).asc(), 
        concat(col("first_name"), lookup("TestLookup", col("customer_id"), col("email")).getField("last_name")).asc()
    )
