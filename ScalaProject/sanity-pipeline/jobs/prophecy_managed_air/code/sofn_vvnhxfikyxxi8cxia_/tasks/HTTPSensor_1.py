def HTTPSensor_1():
    settings = {}
    from airflow.providers.http.sensors.http import HttpSensor

    return HttpSensor(
        task_id = "HTTPSensor_1",
        endpoint = "/webhp",
        request_params = None,
        response_check = None,
        http_conn_id = "rl6j7X9mDUkIrZzdfPx5B",
        poke_interval = 60,
        **settings,
    )
