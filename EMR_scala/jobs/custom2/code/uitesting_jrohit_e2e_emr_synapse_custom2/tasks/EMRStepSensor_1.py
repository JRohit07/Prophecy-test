def EMRStepSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor # noqa
    from datetime import timedelta

    return EmrStepSensor(
        task_id = "EMRStepSensor_1",
        job_flow_id = "{{ ti.xcom_pull('EMRJobFlow_1')}}",
        aws_conn_id = "aws_default",
        step_id = "{{ ti.xcom_pull('EMRAddStep_0')[0] }}",
        **settings,
    )
