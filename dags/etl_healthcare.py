from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

default_args = {
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG('etl_healthcare', schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data
    )
    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data
    )
    load = PythonOperator(
        task_id='load',
        python_callable=load_data
    )

    extract >> transform >> load