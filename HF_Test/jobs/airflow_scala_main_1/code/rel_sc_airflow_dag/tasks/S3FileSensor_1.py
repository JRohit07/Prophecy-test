def S3FileSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
    from datetime import timedelta

    return S3KeySensor(
        task_id = "S3FileSensor_1",
        bucket_key = [
          s.strip()
          for s in "dags/_scala_mwaa_renamed.zip, dags/ash_ashvjit_12_HelloWorld_MWAA_Job_adhoc_3c3b.zip".split(",")
          if s.strip()
        ],
        bucket_name = "prophecy-mwaa-243",
        check_fn = None,
        aws_conn_id = "aws_default",
        wildcard_match = False,
        verify = True,
        **settings,
    )
