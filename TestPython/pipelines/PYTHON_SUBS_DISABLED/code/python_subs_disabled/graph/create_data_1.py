from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def create_data_1(spark: SparkSession) -> DataFrame:
    
    out0 = spark\
               .createDataFrame(
                 [('POST', 'https://countriesnow.space/api/v0.1/countries/capital', """{\"country\": \"nigeria\"}""",
                   "None", None),
                  ('GET', 'https://countriesnow.space/api/v0.1/countries/capital/qas?country=Nigeria',
                   """{\"country\": \"nigeria\"}""", "None", None),
                  ('GET', 'https://rest.coinapi.io/v1/exchangerate/DOGE/USD', """None""",
                   '{"X-CoinAPI-Key":"AC878A71-0493-4883-AC6C-CAC126E84B3E"}', "None"),]
               )\
               .toDF('method', 'url', 'json', 'headers', 'params')

    return out0
