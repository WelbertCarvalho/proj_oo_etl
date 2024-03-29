from pathlib import Path
import requests
import json
import pandas as pd
from datetime import datetime as dt

class Extract:
    def __init__(self):
        print("Instance of extract object\n")

    def get_json_data(self, url):
        r = requests.get(url)
        json_data = json.loads(r.text)
        json_data = dict(json_data[0])
        return json_data

    def create_df_using_json(self, json_data):
        df = pd.DataFrame(json_data, index=[0])
        return df

    def create_df_using_csv(self, csv_path_and_file_name, separator = ','):
        try:
            df = pd.read_csv(csv_path_and_file_name, separator, encoding = 'utf-8')
            print('Used encoding: utf-8')
        except:
            print('Used encoding: latin_1')
            df = pd.read_csv(csv_path_and_file_name, separator, encoding = 'latin_1')
        return df

    def create_csv_using_df(self, df, folder_name, target_file_name):
        path = f'./{folder_name}'
        df.to_csv(
            f'{path}/{target_file_name}.csv',
            index = False,
            sep = ';',
            encoding = 'utf-8',
            header = True
         )
        return f"CSV file created in '{path}/{target_file_name}.csv'"

    def _sql_file_content(self, file_name):
        this_path_file = Path().absolute()
        sql_path = f"{this_path_file}/sql"
        sql_file = open(f"{sql_path}/{file_name}.sql", 'r')
        sql_content = sql_file.read()
        sql_file.close()
        return sql_content
    
    def create_df_reading_sql_file_without_param(self, file_name, connection):
        sql_content = self._sql_file_content(file_name)
        df = pd.read_sql_query(sql_content, connection)
        return df
         
    def create_df_reading_sql_file_with_dates_param(self, file_name, connection, start_date, end_date):
        params = (start_date, end_date)
        sql_content = self._sql_file_content(file_name)
        df = pd.read_sql_query(
            sql = sql_content, 
            con = connection, 
            params = params)
        return df
        