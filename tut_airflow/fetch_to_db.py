"""
Fetch data and store in DB tutorial from Airflow itself: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
"""

import datetime

import pendulum
import requests
from airflow.decorators import dag, task
from airflow.providers.mongo.hooks.mongo import MongoHook


@dag(
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
)
def etl():
    @task
    def get_data():
        data_path = '/tmp/employees.csv'
        url = 'https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/pipeline_example.csv'

        response = requests.get(url)

        with open(data_path, "w") as out_file:
            out_file.write(response.text)

        with open(data_path, "r") as in_file:
            reader = csv.DictReader(in_file)
            rows = [row for row in reader]

        mongo_hook = MongoHook(conn_id='mongo_nowi_test')
        client = mongo_hook.get_conn()
        client['airflow']['employees_temp'].insert_many(rows, ordered=False)
        client.close()

    @task
    def merge_data():
        try:
            mongo_hook = MongoHook(conn_id='mongo_nowi_test')
            client = mongo_hook.get_conn()
            incoming_serial_numbers = client['airflow']['employees_temp'].distinct('Serial Number')
            client['airflow']['employees'].delete_many({"Serial Number": {"$in": incoming_serial_numbers}})
            client['airflow']['employees'].insert_many(client['airflow']['employees_temp'].find({}))
            client.close()
            return 0
        except Exception as exc:
            return 1

    get_data() >> merge_data()


dag = etl()
