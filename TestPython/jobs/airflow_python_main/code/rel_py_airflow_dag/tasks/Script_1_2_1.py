def Script_1_2_1():
    settings = {}
    from datetime import timedelta
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_1_2_1", bash_command = "echo \"hello airflow\"", **settings)
