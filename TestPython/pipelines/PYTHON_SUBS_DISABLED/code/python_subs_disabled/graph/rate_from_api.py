from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_subs_disabled.config.ConfigStore import *
from python_subs_disabled.udfs.UDFs import *

def rate_from_api(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from prophecy.udfs import get_rest_api
    requestDF = in0.withColumn(
        "api_output",
        get_rest_api(
          to_json(struct(lit("GET").alias("method"), col("url"), lit(Config.coin_api_key).alias("headers"))),
          lit("")
        )
    )

    return requestDF.withColumn(
        "content_parsed",
        from_json(col("api_output.content"), schema_of_json(requestDF.select("api_output.content").take(1)[0][0]))
    )
