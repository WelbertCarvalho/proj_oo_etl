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

# creating and printing df before transformation
teste\
     = economic_freedom_2[
        ["Population (Millions)", 
        "GDP (Billions, PPP)", 
        "GDP per Capita (PPP)", 
        "Unemployment (%)", 
        "FDI Inflow (Millions)"]]

print(teste.info())
print(teste.head())

t = Transform()

economic_freedom_transformed\
    = t.transform_columns_type(
        economic_freedom_2,
        [ 
            "GDP (Billions, PPP)", 
            "GDP per Capita (PPP)", 
            "Unemployment (%)", 
            "FDI Inflow (Millions)"
        ], 
        'float')

# creating and printing df after transformation
teste\
     = economic_freedom_transformed[
        ["Population (Millions)", 
        "GDP (Billions, PPP)", 
        "GDP per Capita (PPP)", 
        "Unemployment (%)", 
        "FDI Inflow (Millions)"
        ]
    ]

print(teste.head())
print(teste.info())


# Grouping data
mean_unemployment_region\
    = t.group_data(
        economic_freedom_transformed, 
        "Region", 
        "Unemployment (%)",
        "mean")

print(mean_unemployment_region.head(20))
