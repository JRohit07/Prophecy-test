from test_jrohit_e2e_snowflake_project_external_airflow253.utils import *

def Model_1():
    from airflow.operators.bash import BashOperator
    import os
    import zipfile
    import tempfile

    return BashOperator(
        task_id = "Model_1",
        bash_command = " && ".join(
          ["{} && cd $tmpDir/{}".format(
             (
               "set -euxo pipefail && tmpDir=`mktemp -d` && git clone "
               + "--depth 1 {} --branch {} $tmpDir".format(
                 "https://github.com/JRohit07/Prophecy-test",
                 "__PROJECT_FULL_RELEASE_TAG_PLACEHOLDER__"
               )
             ),
             "SnowflakeTableau"
           ),            "dbt seed --profile run_profile_snowflake -m customers_by_country",            "dbt run --profile run_profile_snowflake -m customers_by_country",            "dbt test --profile run_profile_snowflake -m customers_by_country"]
        ),
        env = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
