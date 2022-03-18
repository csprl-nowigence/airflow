
import pendulum
from airflow.decorators import dag, task

import test_importing.mylib


@dag(
    default_args={
        'owner': 'csprl',
    },
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz='UTC'),
    catchup=False,
    tags=['debugging', 'learning', 'troubleshooting'],
)
def import_with_package():
    @task
    def main_task():
        test_importing.mylib.func1()
        print(test_importing.mylib.func2())
        print(test_importing.mylib.var1)
        print(test_importing.mylib.var2)

    main_task()


this_dag = import_with_package()
