def REL_PY_PIP_SG_SRC():
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "REL_PY_PIP_SG_SRC",
        json = {
          "task_key": "REL_PY_PIP_SG_SRC", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {
              "spark.prophecy.execution.metrics.component-metrics.table": "prophecy.component_runs_manual", 
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/deleteme", 
              "spark.prophecy.execution.metrics.interims.table": "prophecy.interims_manual", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "5295", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.pipeline-metrics.table": "prophecy.pipeline_runs_manual", 
              "spark.prophecy.packages.path": "{\"pipelines/PYTHON_SG_SRC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/REL_PY_PIP_SG_SRC-1.0-py3-none-any.whl\",\"pipelines/EM_DISABLED_PYTHON_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SamplingModel_DisabledAll-1.0-py3-none-any.whl\",\"pipelines/IO_PYTHON_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SamplingMode_IO_All-1.0-py3-none-any.whl\",\"pipelines/PYTHON_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/PYTHON_BASIC-1.0-py3-none-any.whl\"}", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": False, 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.uitesting.prophecy.io/eventws"
            }, 
            "driver_node_type_id": "i3.xlarge"
          }, 
          "python_wheel_task": {
            "package_name": "REL_PY_PIP_SG_SRC", 
            "entry_point": "main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.3"}},                          {"pypi" : {"package" : "prophecy-libs==1.5.9"}},                          {
                           "whl": "dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/REL_PY_PIP_SG_SRC-1.0-py3-none-any.whl"
                         }]
        },
        databricks_conn_id = "dev_databricks_shared_connection",
        **settings
    )
