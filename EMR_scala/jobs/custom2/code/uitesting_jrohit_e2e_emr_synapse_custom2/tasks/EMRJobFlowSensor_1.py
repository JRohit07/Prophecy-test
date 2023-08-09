def EMRJobFlowSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.emr import (EmrJobFlowSensor, ) # noqa
    from datetime import timedelta

    return EmrJobFlowSensor(
        task_id = "EMRJobFlowSensor_1",
        job_flow_id = "{{ ti.xcom_pull('EMRJobFlow_1')}}",
        aws_conn_id = "aws_default",
        **settings,
    )
