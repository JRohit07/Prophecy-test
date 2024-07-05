from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_first.config.ConfigStore import *
from pipeline_first.udfs.UDFs import *

def target_1(spark: SparkSession, in0: DataFrame):
    from pyspark.dbutils import DBUtils
    in0.write\
        .format("jdbc")\
        .option("url", "jdbc:mysql://3.101.152.38:3306/test_database")\
        .option("dbtable", "test_table_destination")\
        .option("user", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("driver", "com.mysql.jdbc.Driver")\
        .mode("overwrite")\
        .save()
