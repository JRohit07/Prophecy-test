import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from uitesting_jrohit_e2e_emr_synapse_customflow.tasks import EMRStepSensor_1
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "uitesting_jrohit_e2e_EMR_Synapse_CustomFlow", 
    schedule_interval = "0 0/1 * * *", 
    default_args = {"owner" : "Prophecy", "ignore_first_depends_on_past" : True, "do_xcom_push" : True}, 
    start_date = pendulum.today('UTC'), 
    catchup = True
) as dag:
    EMRStepSensor_1_op = EMRStepSensor_1()
