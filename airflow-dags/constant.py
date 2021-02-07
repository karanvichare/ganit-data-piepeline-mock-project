# -*- coding: utf-8 -*-

class Constant:
    '''
    Generic Constant is class used to store all string literals
    '''
    # INI FILE PATH and consul constants
    INI_FILE_PATH = 'database_creds.ini'

    DEFINITION = 'DEFINITION'
    STAGE = 'STAGE'

    DB_HOST =  'DB_HOST'
    DB_USERNAME = 'DB_USERNAME'
    DB_PASSWORD = 'DB_PASSWORD'
    DB_NAME = 'DB_NAME'

    DB_CONNECTION_ID = 'DB_CONNECTION_ID'
    AIRFLOW_OWNER = 'AIRFLOW_OWNER'
    CURRENCY_DATA_TABLE_NAME= 'currency_data'
    CURRENCY_INFO = 'currency_types'

    MINUTES = 'RETRY_MINUTES'
    RETRIES = 'RETRIES'

    API_URL = 'API_URL'
    START_DATE = 'START_DATE'

    JSON_OUTPUT_FILE = '/tmp/api_json_data.json'
    CURRENCIES = ['EUR', 'USD', 'JPY', 'CAD', 'GBP', 'NZD','IND','INR']
