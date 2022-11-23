from Connection import Connection
from Extract import Extract

instance_con = Connection()
datalake = instance_con.mysql_datalake_con()
dw = instance_con.mysql_datawarehouse_con()

instance_extract = Extract()
# json_data = instance_extract.get_json_data("https://economia.awesomeapi.com.br/json/daily/USD-BRL/0")
# df = instance_extract.create_df_using_json(json_data)

# df = instance_extract.create_df_using_csv(
#     csv_path_and_file_name\
#          = '/home/welbert/Documents/proj_oo/kaggle_datasets/economic_freedom_index2019_data.csv'
#     )

# df = instance_extract.download_kaggle_dataset(
#     user = "lewisduncan93/the-economic-freedom-index",
#     file_name = "economic_freedom_index2019_data.csv"
# )
  
df_cotacao_moedas = instance_extract\
    .create_df_reading_sql_file_without_param(
    'test_proj_oo_ETL', 
    datalake
    )
