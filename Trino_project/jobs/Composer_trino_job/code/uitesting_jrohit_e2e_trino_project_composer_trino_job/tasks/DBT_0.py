def DBT_0():
    from datetime import timedelta
    from airflow.operators.bash import BashOperator

    return BashOperator(
        task_id = "DBT_0",
        bash_command = "set -euxo pipefail; tmpDir=`mktemp -d`; git clone https://github.com/JRohit07/Prophecy-test --branch br1 --single-branch $tmpDir; cd $tmpDir/Trino_project; dbt run --profile run_profile_trino; dbt test --profile run_profile_trino; ",
        env = {"DBT_PROFILES_DIR" : "/home/airflow/gcs/data"},
        append_env = True,
    )
