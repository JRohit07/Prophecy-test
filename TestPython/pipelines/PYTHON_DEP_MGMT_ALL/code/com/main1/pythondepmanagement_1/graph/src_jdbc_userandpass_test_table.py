from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def src_jdbc_userandpass_test_table(spark: SparkSession) -> DataFrame:
    from pyspark.dbutils import DBUtils

    return spark.read\
        .format("jdbc")\
        .option("url", "jdbc:mysql://3.101.152.38:3306/test_database")\
        .option("user", DBUtils(spark).secrets.get(scope = "qasecrets_mysql", key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = "qasecrets_mysql", key = "password"))\
        .option("dbtable", "test_table")\
        .option("pushDownPredicate", True)\
        .option("driver", "com.mysql.jdbc.Driver")\
        .load()
