def SM_IO_SCALA_BASIC():
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "SM_IO_SCALA_BASIC",
        json = {
          "task_key": "SM_IO_SCALA_BASIC", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {
              "prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/prophecy_managed_air", 
              "prophecy.metadata.is.interactive.run": "false", 
              "prophecy.execution.service.url": "wss://execution.dp.uitesting.prophecy.io/eventws", 
              "prophecy.execution.metrics.disabled": False, 
              "prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "prophecy.execution.metrics.pipeline-metrics.table": "prophecy.pipeline_runs_manual", 
              "prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "prophecy.packages.path": "{\"pipelines/IO_SCALA_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SM_IO_SCALA_BASIC.jar\",\"pipelines/SCALA_DEP_MGMT_ALL\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/REL_SC_PIP_DEP_MGMT_ALL.jar\",\"pipelines/SCALA_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SCALA_BASIC.jar\"}", 
              "prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "prophecy.metadata.fabric.id": "7557", 
              "spark.databricks.isv.product": "prophecy", 
              "prophecy.execution.metrics.interims.table": "prophecy.interims_manual", 
              "prophecy.execution.metrics.component-metrics.table": "prophecy.component_runs_manual"
            }, 
            "driver_node_type_id": "i3.xlarge"
          }, 
          "spark_jar_task": {
            "main_class_name": "com.scalaio.main.job1.Main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.0.50"}},                          {"pypi" : {"package" : "prophecy-libs==1.5.6"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SM_IO_SCALA_BASIC.jar"
                         }]
        },
        databricks_conn_id = "J2cv5ojaMVs5b7hPCHLsD",
        **settings
    )
