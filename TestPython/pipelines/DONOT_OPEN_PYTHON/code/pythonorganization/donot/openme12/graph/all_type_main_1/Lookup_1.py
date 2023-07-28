from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from .config import *
from pythonorganization.donot.openme12.udfs.UDFs import *

def Lookup_1(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''p_short''']
    valueColumns = ['''p_boolean''']
    createLookup("TestLookupSon", in0, spark, keyColumns, valueColumns)
