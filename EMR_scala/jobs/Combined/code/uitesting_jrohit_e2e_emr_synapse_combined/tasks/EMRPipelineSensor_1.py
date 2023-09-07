def EMRPipelineSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.emr import EmrStepSensor # noqa
    from datetime import timedelta

    return EmrStepSensor(
        task_id = "EMRPipelineSensor_1",
        job_flow_id = "{{ ti.xcom_pull('EMRCreateCluster_1') }}",
        aws_conn_id = "aws_default",
        step_id = "{{ ti.xcom_pull('EMRPipeline_0')[0] }}",
        **settings,
    )
