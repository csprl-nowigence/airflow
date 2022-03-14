"""
India disease tracker example from: https://humansofdata.atlan.com/2018/06/apache-airflow-disease-outbreaks-india/
"""

import datetime as dt

import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator

from utils import scrape_web, scrape_pdf, add_to_dataset

BASE_DIR = "/root/airflow_exploration/idt_pipeline"


with DAG(
    dag_id='india_disease_v1',
    default_args={
        "owner": "csprl",
        "depends_on_past": False,
        "start_date": pendulum.datetime(2022, 3, 14, tz="UTC"),
        "provide_context": True,
    },
    schedule_interval="0 0 * * 2",
    max_active_runs=1,
) as dag:
    task_scrape_web = PythonOperator(
        task_id="scrape_web",
        python_callable=scrape_web,
        op_kwargs={'base_dir': BASE_DIR},
        dag=dag,
    )

    task_scrape_pdf = PythonOperator(
        task_id="scrape_pdf",
        python_callable=scrape_pdf,
        op_kwargs={'base_dir': BASE_DIR},
        dag=dag,
    )

    task_add_to_dataset = PythonOperator(
        task_id="add_to_dataset",
        python_callable=add_to_dataset,
        op_kwargs={'base_dir': BASE_DIR},
        dag=dag,
    )

    task_scrape_web.set_downstream(task_scrape_pdf)
    task_scrape_pdf.set_downstream(task_add_to_dataset)
