"""
Fetch data and store in DB tutorial from Airflow: https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html
"""

import csv
import datetime

import pendulum
import requests
from airflow.decorators import dag, task
from airflow.providers.mongo.hooks.mongo import MongoHook

MONGO_CONNECTION_ID = 'mongo_nowi_test'
DB = 'airflow'
EMPLOYEES_COLLECTION = 'employees'
TEMP_COLLECTION = 'employees_temp'


@dag(
    dag_id='fetch_to_db',
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

        for row in rows:
            row['Serial Number'] = int(row['Serial Number'])
            row['Leave'] = int(row['Leave'])

        mongo_hook = MongoHook(conn_id=MONGO_CONNECTION_ID)
        client = mongo_hook.get_conn()
        client[DB][TEMP_COLLECTION].insert_many(rows, ordered=False)
        client.close()

    @task
    def merge_data():
        try:
            mongo_hook = MongoHook(conn_id=MONGO_CONNECTION_ID)
            client = mongo_hook.get_conn()
            incoming_serial_numbers = client[DB][TEMP_COLLECTION].distinct('Serial Number')
            client[DB][EMPLOYEES_COLLECTION].delete_many({"Serial Number": {"$in": incoming_serial_numbers}})
            client[DB][EMPLOYEES_COLLECTION].insert_many(client['airflow'][TEMP_COLLECTION].find({}))
            client.close()
            return 0
        except Exception as e:
            return 1

    @task
    def clear_temp():
        try:
            mongo_hook = MongoHook(conn_id=MONGO_CONNECTION_ID)
            client = mongo_hook.get_conn()
            client['airflow'].drop_collection(TEMP_COLLECTION)
            return 0
        except Exception as e:
            return 1

    get_data() >> merge_data() >> clear_temp()


dag = etl()
