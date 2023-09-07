import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from rel_sc_airflow_dag.tasks import (
    Email_1,
    HTTPSensor_1,
    REL_SC_PIP_DEP_MGMT_ALL,
    S3FileSensor_1,
    SCALA_BASIC,
    SM_IO_SCALA_BASIC,
    Script_1,
    Script_1_1,
    Script_1_2,
    Slack_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "REL_SC_Airflow_DAG", 
    schedule_interval = "0 0 2 2 *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 7, 3, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    SM_IO_SCALA_BASIC_op = SM_IO_SCALA_BASIC()
    Email_1_op = Email_1()
    Slack_1_op = Slack_1()
    HTTPSensor_1_op = HTTPSensor_1()
    Script_1_op = Script_1()
    Script_1_1_op = Script_1_1()
    S3FileSensor_1_op = S3FileSensor_1()
    REL_SC_PIP_DEP_MGMT_ALL_op = REL_SC_PIP_DEP_MGMT_ALL()
    SCALA_BASIC_op = SCALA_BASIC()
    Script_1_2_op = Script_1_2()
    REL_SC_PIP_DEP_MGMT_ALL_op >> [Script_1_1_op, Script_1_2_op]
    SM_IO_SCALA_BASIC_op >> Script_1_op
    Script_1_op >> S3FileSensor_1_op
    SCALA_BASIC_op >> [Email_1_op, HTTPSensor_1_op, REL_SC_PIP_DEP_MGMT_ALL_op]
    Email_1_op >> Slack_1_op
