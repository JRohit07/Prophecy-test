def EMRCreateClusterSensor_1():
    settings = {}
    from airflow.providers.amazon.aws.sensors.emr import (EmrJobFlowSensor, ) # noqa
    from datetime import timedelta

    return EmrJobFlowSensor(
        task_id = "EMRCreateClusterSensor_1",
        job_flow_id = "{{ ti.xcom_pull('EMRCreateCluster_1') }}",
        aws_conn_id = "aws_default",
        target_states = ["WAITING", "RUNNING", "STARTING"],
        failed_states = ["TERMINATED", "TERMINATED_WITH_ERRORS", "TERMINATING"],
        **settings,
    )
