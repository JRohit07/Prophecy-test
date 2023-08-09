import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from uitesting_jrohit_e2e_emr_synapse_combined.tasks import (
    EMRAddStep_0,
    EMRJobFlowSensor_1,
    EMRJobFlow_1,
    EMRStepSensor_1
)
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "uitesting_jrohit_e2e_EMR_Synapse_Combined", 
    schedule_interval = "*/10 8-10 * * *", 
    default_args = {"owner" : "Prophecy", "retries" : 0, "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = True, 
    tags = []
) as dag:
    EMRAddStep_0_op = EMRAddStep_0()
    EMRStepSensor_1_op = EMRStepSensor_1()
    EMRJobFlow_1_op = EMRJobFlow_1()
    EMRJobFlowSensor_1_op = EMRJobFlowSensor_1()
    EMRAddStep_0_op >> EMRStepSensor_1_op
    EMRJobFlow_1_op >> EMRJobFlowSensor_1_op
    EMRJobFlowSensor_1_op >> EMRAddStep_0_op
