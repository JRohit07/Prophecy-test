def SCALA_BASIC():
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "SCALA_BASIC",
        json = {
          "task_key": "SCALA_BASIC", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {
              "spark.prophecy.execution.metrics.component-metrics.table": "prophecy.component_runs_manual", 
              "spark.prophecy.metadata.job.uri": "__PROJECT_ID_PLACEHOLDER__/jobs/airflow_scala_main_1", 
              "spark.prophecy.execution.metrics.interims.table": "prophecy.interims_manual", 
              "spark.prophecy.metadata.is.interactive.run": "false", 
              "spark.prophecy.metadata.fabric.id": "5295", 
              "spark.prophecy.metadata.url": "__PROPHECY_URL_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.pipeline-metrics.table": "prophecy.pipeline_runs_manual", 
              "spark.prophecy.packages.path": "{\"pipelines/IO_SCALA_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SM_IO_SCALA_BASIC.jar\",\"pipelines/SCALA_DEP_MGMT_ALL\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/REL_SC_PIP_DEP_MGMT_ALL.jar\",\"pipelines/SCALA_BASIC\":\"dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SCALA_BASIC.jar\"}", 
              "spark.prophecy.project.id": "__PROJECT_ID_PLACEHOLDER__", 
              "spark.prophecy.execution.metrics.disabled": True, 
              "spark.databricks.isv.product": "prophecy", 
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.uitesting.prophecy.io/eventws"
            }, 
            "driver_node_type_id": "i3.xlarge"
          }, 
          "spark_jar_task": {
            "main_class_name": "com.scala.main.job12.Main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.6"}},                          {"pypi" : {"package" : "prophecy-libs==1.5.10"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/SCALA_BASIC.jar"
                         }]
        },
        databricks_conn_id = "dev_databricks_shared_connection",
        **settings
    )
