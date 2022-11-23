from pathlib import Path
import requests
import json
import pandas as pd

from kaggle.api.kaggle_api_extended import KaggleApi

class Extract:
    def __init__(self):
        print(f"Instance of extract object\n")

    def get_json_data(self, url):
        r = requests.get(url)
        json_data = json.loads(r.text)
        json_data = dict(json_data[0])
        print(json_data)
        return json_data

    def create_df_using_json(self, json_data):
        df = pd.DataFrame(json_data, index=[0])
        print(df.head())
        return df

    def create_df_using_csv(self, csv_path_and_file_name, separator = ','):
        try:
            df = pd.read_csv(csv_path_and_file_name, separator, encoding = 'utf-8')
            print('Used encoding: utf-8')
        except:
            print('Used encoding: latin_1')
            df = pd.read_csv(csv_path_and_file_name, separator, encoding = 'latin_1')
        
        print(df.head())
        return df

    def download_kaggle_dataset(self,user, file_name):
        api = KaggleApi()
        api.authenticate()

        api.dataset_download_file(
            dataset = user,
            file_name = file_name,
            path = './kaggle_datasets',
            force = True
        )
        print(f"The file {file_name} was successfully downloaded")
        return None

    def create_df_reading_sql_file_without_param(self, file_name, connection):
        this_path_file = Path().absolute()
        sql_path = f"{this_path_file}/sql"
        sql_file = open(f"{sql_path}/{file_name}.sql", 'r')
        sql_content = sql_file.read()
        sql_file.close()
        df = pd.read_sql_query(sql_content, connection)
        print(df.head())
        return df
        