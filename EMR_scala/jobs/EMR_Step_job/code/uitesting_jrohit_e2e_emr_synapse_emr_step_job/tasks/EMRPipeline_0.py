def EMRPipeline_0():
    settings = {}
    from datetime import timedelta
    from airflow.providers.amazon.aws.operators.emr import (EmrAddStepsOperator, ) # noqa

    return EmrAddStepsOperator(
        task_id = "EMRPipeline_0",
        job_flow_id = "j-3TRCD2D3YKSKW",
        aws_conn_id = "aws_default",
        steps = [{
           "Name": "pipelines_Synapse_pipeline", 
           "ActionOnFailure": "TERMINATE_CLUSTER", 
           "HadoopJarStep": {
             "Jar": "command-runner.jar", 
             "Args": ["spark-submit",  "--deploy-mode",  "cluster",  "--executor-memory",  "1g",  "--executor-cores",  "1",                        "--num-executors",  "1",  "--driver-memory",  "1g",  "--driver-cores",  "1",  "--conf",                        "spark.prophecy.execution.metrics.disabled=false",  "--jars",                        "s3://prophecy-public-bucket/prophecy-libs/prophecy-libs-assembly-3.2.0-7.1.3.jar",                        "--py-files",                        "s3://prophecy-public-bucket/python-prophecy-libs/prophecy_libs-1.5.9-py3-none-any.whl,s3://prophecy-public-bucket/python-prophecy-libs/pyhocon-0.3.60-py3-none-any.whl,s3://prophecy-public-bucket/python-prophecy-libs/pyparsing-3.1.0-py3-none-any.whl,s3://prophecy-mwaa/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/EMR_pipeline-1.0-py3-none-any.whl",                        "s3://prophecy-mwaa/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/Synapse_pipeline/launcher.py",                        "-i",  "default",  "-O",  "{}"]
           }
         }],
        **settings
    )
