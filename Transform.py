import pandas as pd


class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def transform_columns_type(self, df, columns, target_type):
        # Excluding non-numeric characters in every column of the list
        for column in columns:
            try:
                df[column] = df[column].str.extract('(\d+)', expand = False)
            except:
                print(f"The column named: {column} don't contains non-numeric character.")
                continue

        # Converting every column in the target_type
        for column in columns:
            try:
                df[column] = df[column].astype(target_type)
                print(f"Column: {column} transformed in {target_type} type.")
            except:
                print(f"Column: {column} it's not in a correct format to transform in {target_type} type.")
                continue
    
        return df

    def show_where_is_null(self, df, columns): 
        for column in columns:
            new_df = df[df[column].isnull()]    
            new_df.append(new_df)
        
        return new_df

    def delete_where_is_null_using_index(self, df, df_rows_to_exclude):
        df_new = df[~df.index.isin(df_rows_to_exclude.index)]
        df_new.index = range(df_new.shape[0])
        return df_new

    def filter_data(self, df, column, criteria):
        df_select = df[column] == criteria
        df_new = df[df_select]
        df_new.index = range(df_new.shape[0])
        return df_new

