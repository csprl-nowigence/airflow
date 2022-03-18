import pendulum

from airflow.decorators import dag, task


@dag(
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

)
def my_dag2():
    @task
    def my_task_in_my_dag2():
        print('my_company/my_custom_dags/my_dag2.py:24')

    my_task_in_my_dag2()


this_dag = my_dag2()
