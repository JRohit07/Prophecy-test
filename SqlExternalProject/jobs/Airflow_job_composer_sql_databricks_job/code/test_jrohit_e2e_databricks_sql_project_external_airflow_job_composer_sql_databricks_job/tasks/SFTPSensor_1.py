from test_jrohit_e2e_databricks_sql_project_external_airflow_job_composer_sql_databricks_job.utils import *

def SFTPSensor_1():
    from airflow.providers.sftp.sensors.sftp import SFTPSensor

    return SFTPSensor(
        task_id = "SFTPSensor_1",
        path = "sftp_user/QA/",
        file_pattern = "*.csv",
        sftp_conn_id = "sftp_ashish",
        poke_interval = 60,
        timeout = 600,
    )
