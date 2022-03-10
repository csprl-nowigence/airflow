"""
Airflow tutorial demonstrating the PythonOperator.
"""

from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def my_function(x):
    return f'"{x}" is the value of the parameter.'


with DAG(
    dag_id='python_operator_tutorial',
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
    description='Basic PythonOperator tutorial',
    schedule_interval=timedelta(days=1),
) as dag:
    t1 = PythonOperator(
        task_id='print',
        python_callable=my_function,
        op_kwargs={'x': 'SUPERCALAFRAGILISTICEXPEALIDOCIOUS'},
        dag=dag,
    )

t1
