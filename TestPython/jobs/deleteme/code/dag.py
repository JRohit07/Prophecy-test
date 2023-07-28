import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from h_ec8n2jwoiuq4aul3np0q_.tasks import (
    PYTHON_BASIC,
    PYTHON_BASIC_1,
    REL_PY_PIP_SG_SRC,
    SM_DISABLED_PYTHON_BASIC,
    SM_IO_PYTHON_BASIC
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "H_ec8N2jWOIUQ4AUl3nP0Q_", 
    schedule_interval = "0 0/1 * * *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True, "pool" : "n7pJN9mh"}, 
    start_date = pendulum.datetime(2023, 7, 3, tz = "UTC"), 
    end_date = pendulum.datetime(2023, 7, 10, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    REL_PY_PIP_SG_SRC_op = REL_PY_PIP_SG_SRC()
    SM_DISABLED_PYTHON_BASIC_op = SM_DISABLED_PYTHON_BASIC()
    SM_IO_PYTHON_BASIC_op = SM_IO_PYTHON_BASIC()
    PYTHON_BASIC_op = PYTHON_BASIC()
    PYTHON_BASIC_1_op = PYTHON_BASIC_1()
    SM_IO_PYTHON_BASIC_op >> [REL_PY_PIP_SG_SRC_op, SM_DISABLED_PYTHON_BASIC_op]
    REL_PY_PIP_SG_SRC_op >> PYTHON_BASIC_op
    SM_DISABLED_PYTHON_BASIC_op >> PYTHON_BASIC_1_op
