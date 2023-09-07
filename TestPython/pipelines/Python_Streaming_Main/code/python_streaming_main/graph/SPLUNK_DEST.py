from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def SPLUNK_DEST(spark: SparkSession, in0: DataFrame):
    from prophecy.utils import splunkHECForEachWriter # noqa
    in0.writeStream\
        .option("checkpointLocation", "/tmp/random/testrelease/check_123")\
        .queryName("SPLUNK_DEST_Nc3_rHK3GvIDm0ZaVLuaa$$3ko06WHEDFVLJdtZHwAm1")\
        .foreachBatch(
          splunkHECForEachWriter(
            {
              'url': "http://ec2-3-22-233-65.us-east-2.compute.amazonaws.com:8000/",
              'token': "28d00425-3400-468b-ad4b-52a458b33e9a",
              'backoffFactor': "1",
              'maxRetries': "10",
              'maxPayload': None,
              'stopOnFailure': False,
              'skipSsl': True,
              'certFilePath': None
            }
          )
        )\
        .start()
