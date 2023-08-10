def EMRClusterSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.emr import (EmrJobFlowSensor, ) # noqa
    from datetime import timedelta

    return EmrJobFlowSensor(
        task_id = "EMRClusterSensor_1",
        job_flow_id = "{{ ti.xcom_pull('EMRCreateCluster_1') }}",
        aws_conn_id = "aws_default",
        target_states = ["STARTING", "RUNNING", "WAITING"],
        failed_states = ["TERMINATING", "TERMINATED", "TERMINATED_WITH_ERRORS"],
        **settings,
    )
