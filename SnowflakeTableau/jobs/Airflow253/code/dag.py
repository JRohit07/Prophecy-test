import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from test_jrohit_e2e_snowflake_project_external_airflow253.tasks import Model_1, SFTPSensor_0, SFTPToSnowflake_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "test_jrohit_e2e_Snowflake_Project_external_Airflow253", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1, 
    tags = []
) as dag:
    SFTPSensor_0_op = SFTPSensor_0()
    SFTPToSnowflake_1_op = SFTPToSnowflake_1()
    Model_1_op = Model_1()
    SFTPSensor_0_op >> SFTPToSnowflake_1_op
    SFTPToSnowflake_1_op >> Model_1_op
