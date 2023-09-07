import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from rel_py_airflow_dag.tasks import (
    Email_1,
    HTTPSensor_1,
    PYTHON_BASIC,
    PYTHON_BASIC_1,
    REL_PY_PIP_SG_SRC,
    S3FileSensor_1,
    SM_DISABLED_PYTHON_BASIC,
    SM_IO_PYTHON_BASIC,
    Script_1,
    Script_1_1,
    Script_1_2,
    Script_1_2_1,
    Slack_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "REL_PY_Airflow_DAG", 
    schedule_interval = "0 0 2 1 *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.datetime(2023, 7, 3, tz = "UTC"), 
    end_date = pendulum.datetime(2025, 7, 3, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    REL_PY_PIP_SG_SRC_op = REL_PY_PIP_SG_SRC()
    S3FileSensor_1_op = S3FileSensor_1()
    PYTHON_BASIC_op = PYTHON_BASIC()
    HTTPSensor_1_op = HTTPSensor_1()
    PYTHON_BASIC_1_op = PYTHON_BASIC_1()
    SM_IO_PYTHON_BASIC_op = SM_IO_PYTHON_BASIC()
    Script_1_1_op = Script_1_1()
    Script_1_op = Script_1()
    Script_1_2_1_op = Script_1_2_1()
    Email_1_op = Email_1()
    Slack_1_op = Slack_1()
    SM_DISABLED_PYTHON_BASIC_op = SM_DISABLED_PYTHON_BASIC()
    Script_1_2_op = Script_1_2()
    SM_IO_PYTHON_BASIC_op >> [HTTPSensor_1_op, SM_DISABLED_PYTHON_BASIC_op, Script_1_op]
    Script_1_1_op >> PYTHON_BASIC_op
    HTTPSensor_1_op >> REL_PY_PIP_SG_SRC_op
    REL_PY_PIP_SG_SRC_op >> Email_1_op
    SM_DISABLED_PYTHON_BASIC_op >> S3FileSensor_1_op
    S3FileSensor_1_op >> Script_1_2_op
    Script_1_2_op >> PYTHON_BASIC_1_op
    Script_1_op >> [Script_1_1_op, Slack_1_op]
    PYTHON_BASIC_1_op >> Script_1_2_1_op
