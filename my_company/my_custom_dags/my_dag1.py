import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

# from my_company.common_package.common_module import cm_var
# from my_company.common_package.subpackage.subpackaged_util_module import spum_var
# from my_company.my_custom_dags.base_dag import my_base_function


def my_function():
    print("my_company.my_custom_dags.my_dag1.my_function")


with DAG(
    dag_id='my_company.my_custom_dags.my_dag1.dag',
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
        task_id='my_dag1.t1',
        python_callable=my_function,
        dag=dag
    )

    t1
