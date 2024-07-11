from uitesting_abhisheks_e2etests_snowflake_project_hotfix_airflow.utils import *

def Model_1():
    from airflow.operators.bash import BashOperator
    from datetime import timedelta
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
             "snowflake_project"
           ),            "dbt seed --profile run_profile_snowflake",  "dbt run --profile run_profile_snowflake",            "dbt test --profile run_profile_snowflake"]
        ),
        env = {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy", "DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
