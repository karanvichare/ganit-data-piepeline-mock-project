#imports
from datetime import timedelta , datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from constant import Constant
import configparser
import os
from read_config import Config
from export_api_data import export_data_to_json
from clean_and_load_data import clean_n_load

config , stage = Config.config , Config.stage

default_args = {
    'owner': config.get(stage, Constant.AIRFLOW_OWNER),
    'start_date': datetime.now() - timedelta(hours=6),
    'depends_on_past': False,
    'email': ['karanvichare13@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': int(config.get(stage, Constant.RETRIES)),
    'retry_delay': timedelta(minutes=int(config.get(stage, Constant.MINUTES))),
    'catchup_by_default': False,
}

dag = DAG(
    'fetch_data',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)

start_operator = DummyOperator(task_id='Start_Execution',  dag=dag)

export_data = PythonOperator(
    task_id='export_data_to_json',
    python_callable=export_data_to_json,
    dag=dag,
)


clean_n_ingest_data = PythonOperator(
    task_id='clean_and_load_to_database',
    python_callable=clean_n_load,
    dag=dag,
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

# task dependencies
start_operator >> export_data
export_data >> clean_n_ingest_data
clean_n_ingest_data >> end_operator
