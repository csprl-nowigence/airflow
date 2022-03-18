
import test_importing.mylib

from datetime import timedelta
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator


def a_function():
    test_importing.mylib.func1()
    print(test_importing.mylib.func2())
    print(test_importing.mylib.var1)
    print(test_importing.mylib.var2)


with DAG(
    dag_id='import_lib_with_package_name',
    default_args={
        'owner': 'csprl',
        'depends_on_past': False,
        'start_date': pendulum.datetime(2022,3,1),
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'retry_delay': timedelta(minutes=5),
    },
    description='Import from local package with package name',
    schedule_interval=timedelta(days=1),
) as dag:
    t1 = PythonOperator(
        task_id='call_a_function',
        python_callable=a_function,
        dag=dag,
    )

    t1

