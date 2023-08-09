def EMRJobFlow_1():
    settings = {}
    from airflow.providers.amazon.aws.operators.emr import (EmrCreateJobFlowOperator, )
    from datetime import timedelta

    return EmrCreateJobFlowOperator(
        task_id = "EMRJobFlow_1",
        aws_conn_id = "aws_default",
        emr_conn_id = "emr_small",
        job_flow_overrides = {
          "Name": "PropohecyDevEmr-Demo",
          "ReleaseLabel": "emr-6.11.0",
          "Applications": [{"Name" : "Spark"}, {"Name" : "Livy"}],
        },
        **settings
    )
