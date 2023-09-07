def HTTPSensor_1():
    settings = {}
    from airflow.providers.http.sensors.http import HttpSensor
    from datetime import timedelta

    return HttpSensor(
        task_id = "HTTPSensor_1",
        endpoint = "/webhp",
        request_params = None,
        response_check = lambda response: response.status_code == 200,
        http_conn_id = "http_default",
        poke_interval = 20,
        **settings,
    )
