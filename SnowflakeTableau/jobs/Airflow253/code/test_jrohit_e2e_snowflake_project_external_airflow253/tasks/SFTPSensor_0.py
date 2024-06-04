from test_jrohit_e2e_snowflake_project_external_airflow253.utils import *

def SFTPSensor_0():
    from airflow.providers.sftp.sensors.sftp import SFTPSensor

    return SFTPSensor(
        task_id = "SFTPSensor_0",
        path = "/sftp_user/QA/CustomersDatasetInput.csv",
        sftp_conn_id = "sftp_ashish",
        poke_interval = 60,
        timeout = 600,
    )
