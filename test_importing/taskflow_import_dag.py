
import pendulum
from airflow.decorators import dag, task

import mylib


@dag(
    default_args={
        'owner': 'csprl',
    },
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz='UTC'),
    catchup=False,
    tags=['debugging', 'learning', 'troubleshooting'],
)
def import_no_package():
    @task
    def main_task():
        mylib.func1()
        print(mylib.func2())
        print(mylib.var1)
        print(mylib.var2)

    main_task()


this_dag = import_no_package()
