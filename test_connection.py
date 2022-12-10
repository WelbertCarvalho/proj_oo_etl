from Connection import Connection
from Extract import Extract

instance_con = Connection()
datalake = instance_con.mysql_con('datalake')
dw = instance_con.mysql_con('data_warehouse')

instance_extract = Extract()
# json_data = instance_extract.get_json_data("https://economia.awesomeapi.com.br/json/daily/USD-BRL/0")
# df = instance_extract.create_df_using_json(json_data)

# economic_freedom = instance_extract.create_df_using_csv(
#     csv_path_and_file_name\
#          = '/home/welbert/Documents/proj_oo/kaggle_datasets/economic_freedom_index2019_data.csv'
#     )

# df = instance_extract.download_kaggle_dataset(
#     user = "lewisduncan93/the-economic-freedom-index",
#     file_name = "economic_freedom_index2019_data.csv"
# )
  
# instance_extract\
#     .create_csv_using_df(
#         economic_freedom, 
#         'economic_freedom_test_file'
#         )


# economic_freedom_2 = instance_extract.create_df_using_csv(
#     csv_path_and_file_name\
#          = '/home/welbert/Documents/proj_oo/exported_datasets/economic_freedom_test_file.csv',
#          separator = ';'
#     )

df_cotacao_moedas = instance_extract\
    .create_df_reading_sql_file_without_param(
    'test_proj_oo_ETL', 
    datalake
    )

# df_cotacao_moedas = instance_extract\
#     .create_df_reading_sql_file_with_dates_param(
#         file_name = 'test_proj_oo_ETL_with_params', 
#         connection = datalake, 
#         start_date = '2022-11-01', 
#         end_date = '2022-12-01') 