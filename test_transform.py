from Connection import Connection
from Extract import Extract
from Transform import Transform

instance_con = Connection()
datalake = instance_con.mysql_con('datalake')
dw = instance_con.mysql_con('data_warehouse')

instance_extract = Extract()


economic_freedom_2 = instance_extract.create_df_using_csv(
    csv_path_and_file_name\
         = '/home/welbert/Documents/proj_oo/exported_datasets/economic_freedom_test_file.csv',
         separator = ';'
    )



# t = Transform()
# economic_freedom_transformed = t.replace_specific_characters(economic_freedom_2, "GDP (Billions, PPP)")
teste = economic_freedom_2["GDP (Billions, PPP)"].replace(["$"], "", inplace = True)


teste = economic_freedom_2[["Population (Millions)", "GDP (Billions, PPP)", "GDP per Capita (PPP)", "Unemployment (%)", "FDI Inflow (Millions)"]]


print(teste.head())
print(teste.info())






