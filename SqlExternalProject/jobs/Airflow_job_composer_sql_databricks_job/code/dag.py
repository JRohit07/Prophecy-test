import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from test_jrohit_e2e_databricks_sql_project_external_airflow_job_composer_sql_databricks_job.tasks import (
    Model_0,
    SFTPSensor_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "test_jrohit_e2e_databricks_sql_project_external_Airflow_job_composer_sql_databricks_job", 
    schedule_interval = None, 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = False, 
    max_active_runs = 1
) as dag:
    SFTPSensor_1_op = SFTPSensor_1()
    Model_0_op = Model_0()
    SFTPSensor_1_op >> Model_0_op
