"""
Airflow tutorial demonstrating the use of variables.
"""

from collections import Counter
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models import Variable


def my_function() -> Counter:
    data_path = Variable.get('data_path')
    with open(data_path) as f:
        data = Counter(f.read().split())
    return data


with DAG(
    dag_id='variables_tutorial',
    default_args={
        'owner': 'csprl',
        'depends_on_past': False,
        'start_date': days_ago(2),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='Basic variables tutorial',
    schedule_interval=timedelta(days=1),
) as dag:
    t1 = PythonOperator(
        task_id='word_count',
        python_callable=my_function,
        dag=dag,
    )

t1
