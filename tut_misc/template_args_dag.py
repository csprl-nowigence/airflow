"""
Checking out type and format of template arguments.
"""

import pendulum
from airflow.decorators import dag, task


@dag(
    default_args={
        "owner": "csprl",
    },
    schedule_interval=None,
        start_date=pendulum.datetime(2022, 3, 21, tz='UTC'),
        catchup=False,
        tags=['template', 'tutorial', 'taskflow'],
)
def template_args_dag_v1():
    """Simple taskflow to print template arguments types and values"""
    @task
    def print_template_args(**kwargs):
        for key, value in kwargs.items():
            print(key, f"({type(value)}):", value)

    print_template_args()


this_dag = template_args_dag_v1()
