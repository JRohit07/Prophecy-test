from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def QA_KAFKA_Dest(spark: SparkSession, in0: DataFrame):
    df1 = in0.select([to_json(struct("*")).cast('string').alias("value")])
    writer = df1.writeStream\
                 .format("kafka")\
                 .option("checkpointLocation", "dbfs:/tmp/e2e/streaming_qa_kafka/uitesting")
    writer = writer.outputMode("complete")
    writer\
        .options(
          **{
            "kafka.sasl.jaas.config": "kafkashaded.org.apache.kafka.common.security.scram.ScramLoginModule required username=\"ehtbzofh\" password=\"ho5NvESLghrW69UKaRlqe118Co9OzUV3\";",
            "kafka.sasl.mechanism": "SCRAM-SHA-512",
            "kafka.security.protocol": "SASL_SSL",
            "kafka.bootstrap.servers": "dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094",
            "topic": "ehtbzofh-test-topic-1-target",
          }
        )\
        .start()
