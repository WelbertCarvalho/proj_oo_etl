from Connection import Connection
from Extract import Extract

instance_con = Connection()
datalake = instance_con.mysql_datalake_con()
dw = instance_con.mysql_datawarehouse_con()

instance_extract = Extract()
json_data = instance_extract.get_json_data("https://economia.awesomeapi.com.br/json/daily/USD-BRL/0")
df = instance_extract.create_dataframe_using_json(json_data)

df = instance_extract.create_dataframe_using_csv(
    csv_path_and_file_name = 'put_the_path/and_file_name_with_extension',
    separator = ';'
    )

df = instance_extract.download_kaggle_dataset(
    user = "lewisduncan93/the-economic-freedom-index",
    file_name = "economic_freedom_index2019_data.csv"
)
  