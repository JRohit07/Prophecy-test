def SnowflakeSQL_0():
    from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator # noqa

    return SnowflakeOperator(
        task_id = "SnowflakeSQL_0",
        sql = "select * from CUSTOMER",
        snowflake_conn_id = "snowflake_CICDAccount",
        warehouse = "wrong_WAREHOUSE".strip(),
        database = "wrong_database".strip(),
        schema = "wrong_schema".strip(),
    )
