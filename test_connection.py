from Connection import Connection
from Extract import Extract

instance_con = Connection()
datalake = instance_con.mysql_con('datalake')
dw = instance_con.mysql_con('data_warehouse')

instance_extract = Extract()
economic_freedom_2 = instance_extract.create_df_using_csv(
    csv_path_and_file_name\
         = '/home/welbert/Documents/proj_oo/exported_datasets/economic_freedom_test_file.csv',
         separator = ';'
    )
