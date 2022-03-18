"""
Prints various paths for debugging and troubleshooting purposes.
(why can't I import a module????????)
"""

import pprint
import os
import sys

import pendulum
from airflow.decorators import dag, task


@dag(
    default_args={
        'owner': 'csprl',
    },
    schedule_interval=None,
    start_date=pendulum.datetime(2022, 1, 1, tz='UTC'),
    catchup=False,
    tags=['debugging', 'learning', 'troubleshooting'],
)
def paths_printer_dag_v1():
    """
    Simple DAG to print paths that python / airflow should make available for importing modules.

    Path information gathered from Airflow's [Module Management documentation]
    (https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html)
    """
    @task
    def print_paths():
        """
        Prints PYTHONPATH, sys.path,
        """
        pprint('PYTHONPATH')
        pprint(os.getenv('PYTHONPATH'))
        pprint('sys.path')
        pprint(sys.path)

    print_paths()


this_dag = paths_printer_dag_v1()
