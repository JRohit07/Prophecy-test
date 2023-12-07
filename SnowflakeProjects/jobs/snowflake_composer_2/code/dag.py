import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from staging_jrohit_snowflake_project_external_git_snowflake_composer_2.tasks import SnowflakeSQL_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "staging_jrohit_Snowflake_project_external_git_snowflake_composer_2", 
    schedule_interval = "0 15/1 * * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('Asia/Calcutta'), 
    catchup = True, 
    tags = []
) as dag:
    SnowflakeSQL_0_op = SnowflakeSQL_0()
