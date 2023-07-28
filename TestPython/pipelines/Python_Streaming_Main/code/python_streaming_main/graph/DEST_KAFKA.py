from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def DEST_KAFKA(spark: SparkSession, in0: DataFrame):
    df1 = in0.select([to_json(struct("*")).cast('string').alias("value")])
    writer = df1.writeStream.format("kafka").option("checkpointLocation", "dbfs:/tmp/randomcheck/qa_dest_kafka")
    writer = writer.outputMode("complete")
    writer\
        .options(
          **{
            "kafka.sasl.jaas.config": "kafkashaded.org.apache.kafka.common.security.scram.ScramLoginModule required username=\"rxiuwdvx\" password=\"nEnzuoVESMBR1hrGZxec_-4BlWsHJ9Bo\";",
            "kafka.sasl.mechanism": "SCRAM-SHA-256",
            "kafka.security.protocol": "SASL_SSL",
            "kafka.bootstrap.servers": "dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094",
            "topic": "rxiuwdvx-test-target",
          }
        )\
        .start()
