import pandas as pd
import json
from constant import Constant
from read_config import Config
from sqlalchemy import create_engine

config, stage = Config.config, Config.stage


class DataTranformation():
    def __init__(self):
        self.json_data_path = Constant.JSON_OUTPUT_FILE
        self.currency_to_process = Constant.CURRENCIES
        self.conection_details="""mysql+pymysql://{0}:{1}@/{2}?{3}""".format(config.get(stage, 'DB_USERNAME'),str(config.get(stage, 'DB_PASSWORD')),config.get(stage, 'DB_NAME'),config.get(stage, 'DB_HOST'))

    def read_data(self):
        with open(self.json_data_path) as f:
            data = json.load(f)
        return data

    def transform_to_dataframe(self, data):
        df = pd.DataFrame.from_dict(data["rates"], orient='index')
        df[data['base']] = 1
        df = df.rename_axis('DATE').reset_index()
        return df

    def filter_data(self, df):
        df.columns = map(str.upper, df.columns)
        columns_matching = list(
            set(self.currency_to_process).intersection(df.columns))
        
        columns_matching.append('DATE')
        filtered_df = df[columns_matching]
        return filtered_df

    def melt_data(self, df):
        df = df.melt(id_vars=["DATE"],
                      var_name="currency_type",
                      value_name="value")
        return df

    def ingest_data(self, df ,tablename):        
        # print(self.conection_details)
        engine=create_engine(self.conection_details,echo=False)
        df.to_sql(name=tablename,con=engine,if_exists='replace', chunksize=1000,index=False)


def clean_n_load():
    try: 
        transform = DataTranformation()
        #Function to reda data from json file
        data = transform.read_data()

        #Function to transform json object to dataframe
        df = transform.transform_to_dataframe(data)

        #Function to filter required currencies
        df = transform.filter_data(df)

        #Function to melt data to store in database
        df = transform.melt_data(df)

        #Remove duplicates to clean data 
        df = df.drop_duplicates()

        #Function to ingest currency data table to database
        transform.ingest_data(df,Constant.CURRENCY_DATA_TABLE_NAME)

        #Create second table to store all unique currency types
        currency_type = pd.DataFrame(df.currency_type.unique(),columns=["currency_type"])
        currency_type['type_id'] = range(1, len(currency_type) + 1)

        #Function to ingest currency types table to database
        transform.ingest_data(currency_type,Constant.CURRENCY_INFO)
    except Exception as e:
        raise(e)

