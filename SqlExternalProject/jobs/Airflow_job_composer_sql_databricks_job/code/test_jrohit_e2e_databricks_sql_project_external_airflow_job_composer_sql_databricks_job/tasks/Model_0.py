from test_jrohit_e2e_databricks_sql_project_external_airflow_job_composer_sql_databricks_job.utils import *

def Model_0():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile

    return BashOperator(
        task_id = "Model_0",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "{} --branch {} --single-branch $tmpDir".format(
                 "https://github.com/JRohit07/Prophecy-test",
                 "main"
               )
             ),
             "SqlExternalProject"
           ),            "dbt seed --profile run_profile -m customer_orders",            "dbt run --profile run_profile -m customer_orders",            "dbt test --profile run_profile -m customer_orders"]
        ),
        env = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
