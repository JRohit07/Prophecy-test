from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from secondpipeline.config.ConfigStore import *
from secondpipeline.udfs.UDFs import *

def target_2(spark: SparkSession, in0: DataFrame):
    from pyspark.dbutils import DBUtils
    in0.write\
        .format("jdbc")\
        .option("url", f"jdbc:mysql://3.101.152.38:3306/{Config.JDBC_DATABASE}")\
        .option("dbtable", f"{Config.TEST}_table_destination")\
        .option("user", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "username"))\
        .option("password", DBUtils(spark).secrets.get(scope = "rohit_mysql", key = "password"))\
        .option("driver", "com.mysql.jdbc.Driver")\
        .mode("overwrite")\
        .save()
