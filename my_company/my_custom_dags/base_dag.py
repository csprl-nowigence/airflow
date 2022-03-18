
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator


def my_base_function():
    print("my_company.my_custom_dags.base_dag.my_function")


with DAG(
    dag_id='my_company.my_custom_dags.base_dag.dag',
    default_args={
        'owner': 'csprl',
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
    },
    description='A simple tutorial DAG',
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 3, 1),
    catchup=False,
    tags=['troubleshooting', 'imports'],
) as dag:
    t1 = PythonOperator(
        task_id='base_dag1.t1',
        python_callable=my_base_function,
        dag=dag
    )

    t1
