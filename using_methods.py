from Connection import Connection
from Extract import Extract
from Transform import Transform


# Creating an instance of the connection object
instance_con = Connection()
datalake = instance_con.mysql_con('datalake')
dw = instance_con.mysql_con('data_warehouse')


# Creating an instance of the extract object
instance_extract = Extract()


# Creating a dataframe using a local csv
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

# Printing Information before apply the transformation in the teste df
print(teste.info())
print(teste.head())


# Creating an instance of transform object and transforming the float columns
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

# Printing Information after transformation
print(teste.head())
print(teste.info())


# Grouping and printing data
mean_unemployment_region\
    = t.group_data(
        economic_freedom_transformed, 
        "Region", 
        "Unemployment (%)",
        "count")

print(mean_unemployment_region.head(20))

# Filtering and printing df
data_filtered = t.filter_data(
    economic_freedom_transformed, 
    'Region', 
    'Europe'
    )

print(data_filtered.head())

# Total lines in a dataframe
total_rows_Europe = t.df_total_rows(data_filtered)
print(total_rows_Europe)

