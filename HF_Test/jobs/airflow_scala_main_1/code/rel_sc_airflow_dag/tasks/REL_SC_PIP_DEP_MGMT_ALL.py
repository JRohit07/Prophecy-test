def REL_SC_PIP_DEP_MGMT_ALL():
    settings = {}
    from datetime import timedelta
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "REL_SC_PIP_DEP_MGMT_ALL",
        json = {
          "task_key": "REL_SC_PIP_DEP_MGMT_ALL", 
          "new_cluster": {
            "ssh_public_keys": [], 
            "node_type_id": "m5.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "runtime_engine": "STANDARD", 
            "custom_tags": {}, 
            "autoscale": {"min_workers" : 1, "max_workers" : 2}, 
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
              "spark.prophecy.metadata.job.branch": "__PROJECT_RELEASE_VERSION_PLACEHOLDER__", 
              "spark.prophecy.execution.service.url": "wss://execution.dp.uitesting.prophecy.io/eventws"
            }, 
            "init_scripts": [], 
            "driver_node_type_id": "r5.xlarge", 
            "cluster_source": "UI", 
            "aws_attributes": {
              "ebs_volume_count": 1, 
              "availability": "SPOT_WITH_FALLBACK", 
              "first_on_demand": 2, 
              "ebs_volume_type": "THROUGHPUT_OPTIMIZED_HDD", 
              "spot_bid_price_percent": 99, 
              "zone_id": "us-east-1f", 
              "ebs_volume_size": 500
            }, 
            "spark_env_vars": {"PYSPARK_PYTHON" : "/databricks/python3/bin/python3"}, 
            "enable_elastic_disk": False
          }, 
          "spark_jar_task": {
            "main_class_name": "org.main.scla_dep_mgmt_change.Main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.1.6"}},                          {"pypi" : {"package" : "prophecy-libs==1.5.10"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/prophecy/uitesting/__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__/pipeline/REL_SC_PIP_DEP_MGMT_ALL.jar"
                         },                          {"maven" : {"coordinates" : "mysql:mysql-connector-java:8.0.29", "exclusions" : []}},                          {"maven" : {"coordinates" : "org.typelevel:cats-core_2.12:2.6.1", "exclusions" : []}},                          {"maven" : {"coordinates" : "org.apache.spark:spark-mllib_2.12:3.3.0", "exclusions" : []}},                          {"maven" : {"coordinates" : "com.crealytics:spark-excel_2.12:3.3.1_0.18.7", "exclusions" : []}}]
        },
        databricks_conn_id = "dev_databricks_connection",
        **settings
    )
