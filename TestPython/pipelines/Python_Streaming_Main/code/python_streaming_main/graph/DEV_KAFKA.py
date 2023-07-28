from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DEV_KAFKA(spark: SparkSession) -> DataFrame:
    consumer_options = {
        "kafka.sasl.jaas.config": "kafkashaded.org.apache.kafka.common.security.scram.ScramLoginModule required username=\"rxiuwdvx\" password=\"nEnzuoVESMBR1hrGZxec_-4BlWsHJ9Bo\";",
        "kafka.sasl.mechanism": "SCRAM-SHA-256",
        "kafka.security.protocol": "SASL_SSL",
        "kafka.bootstrap.servers": "dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094",
        "kafka.session.timeout.ms": "6000",
        "group.id": "",
    }
    consumer_options["subscribe"] = "rxiuwdvx-demo-producer"
    consumer_options["startingOffsets"] = "earliest"
    consumer_options["includeHeaders"] = False

    return (spark.readStream\
        .format("kafka")\
        .options(**consumer_options)\
        .load()\
        .withColumn("value", col("value").cast("string"))\
        .withColumn("key", col("key").cast("string")))\
        .withColumn("value", from_json(
        col("value"),
        schema_of_json(
          "{\"order_id\": 966476, \"customer_id\": 6, \"order_status\": \"Pending\", \"order_category\": \"Sales\", \"order_date\": \"2003-12-05\", \"amount\": 35967.42}"
        )
    ))
