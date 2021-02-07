from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from constant import Constant
import configparser
from read_config import Config

config , stage = Config.config , Config.stage

db_connection_id = config.get(stage, Constant.DB_CONNECTION_ID)  

database_name = config.get(stage, Constant.DB_NAME) 
currency_data_table = Constant.CURRENCY_DATA_TABLE_NAME
all_currencies_table = Constant.CURRENCY_INFO

default_args = {
    'owner': config.get(stage, Constant.AIRFLOW_OWNER),
    'start_date': datetime.now() - timedelta(hours=6),
    'depends_on_past': False,
    'email_on_retry': False,
    'retries': int(config.get(stage, Constant.RETRIES)),
    'retry_delay': timedelta(minutes=int(config.get(stage, Constant.MINUTES))),
    'catchup_by_default': False,
}

dag = DAG('create_database_n_tables',
          default_args=default_args,
          description='Create curreny types table in mysql database using Airflow',
          schedule_interval=None,
          max_active_runs=1
          )

start_operator = DummyOperator(task_id='Start_Execution',  dag=dag)

create_database = MySqlOperator(
    task_id="create_database",
    dag=dag,
    mysql_conn_id=db_connection_id,
    sql='''
    CREATE DATABASE IF NOT EXISTS `{0}`;
    '''.format(database_name)
)

create_currency_types_table = MySqlOperator(
    task_id="create_currency_types_table",
    dag=dag,
    mysql_conn_id=db_connection_id,
    sql='''
    CREATE TABLE IF NOT EXISTS {0}.{1} (
    	currency_type varchar(255),
        type_id int  NOT NULL AUTO_INCREMENT,
        PRIMARY KEY (type_id)
    );
    '''.format(database_name,all_currencies_table)
)

create_currency_data_table = MySqlOperator(
    task_id="create_currency_data_table",
    dag=dag,
    mysql_conn_id=db_connection_id,
    sql='''
    CREATE TABLE IF NOT EXISTS {0}.{1} (
    	DATE Date,
        value float,
        currency_type  varchar(255)
    );
    '''.format(database_name,currency_data_table)
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

# task dependencies
start_operator >> create_database
create_database >> create_currency_types_table
create_currency_types_table >> create_currency_data_table
create_currency_data_table >> end_operator
