"""
Tutorial from https://www.analyticsvidhya.com/blog/2020/11/getting-started-with-apache-airflow/
modified to just run a bash command instead of installing some cricket scores package.
"""

from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

dag = DAG(
    dag_id="netstat-plant",
    default_args={
        'owner': 'csprl',
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
    description='simple bash command `netstat -plant`',
    schedule_interval=timedelta(days=1)
)

t1 = BashOperator(
    task_id='print_label',
    bash_command='echo CURRENT OPEN PORTS',
    dag=dag
)

t2 = BashOperator(
    task_id='netstat',
    bash_command='netstat -plant',
    dag=dag
)

t1 >> t2
