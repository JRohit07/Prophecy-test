from r_q82ilbifjh93t2u48k_g_.utils import *

def Model_0():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "Model_0",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": True,
          "run_deps": False,
          "run_seeds": True,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": "14304",
          "git_entity": "branch",
          "git_entity_value": "devNewTests",
          "git_ssh_url": "https://github.com/JRohit07/Prophecy-test",
          "git_sub_path": "GenericTestStaging",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": " --profile run_profile",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}, 
          "git_token_secret": "VKPYZO8SkMM7foBMzspE3w_", 
          "dbt_profile_secret": "NBGW5z7eP5DyFVJyclt-j"
        },
    )
