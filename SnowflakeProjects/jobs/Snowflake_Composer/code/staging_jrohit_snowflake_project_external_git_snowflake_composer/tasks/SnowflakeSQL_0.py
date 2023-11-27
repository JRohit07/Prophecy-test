def SnowflakeSQL_0():
    from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator # noqa

    return SnowflakeOperator(
        task_id = "SnowflakeSQL_0",
        sql = "select * from ITEM",
        snowflake_conn_id = "snowflake_CICD",
        warehouse = "COMPUTE_WH".strip(),
        database = "QA_DATABASE".strip(),
        schema = "QA_SCHEMA".strip(),
    )
