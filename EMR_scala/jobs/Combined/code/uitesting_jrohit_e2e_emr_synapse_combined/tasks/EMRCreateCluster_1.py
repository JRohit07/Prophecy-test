def EMRCreateCluster_1():
    settings = {}
    from airflow.providers.amazon.aws.operators.emr import (EmrCreateJobFlowOperator, )
    from datetime import timedelta

    return EmrCreateJobFlowOperator(
        task_id = "EMRCreateCluster_1",
        aws_conn_id = "aws_default",
        emr_conn_id = "emr_small",
        job_flow_overrides = {},
        **settings
    )
