from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Lookup_1(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''p_short''']
    valueColumns = ['''p_boolean''']
    createLookup("TestLookupSon", in0, spark, keyColumns, valueColumns)
