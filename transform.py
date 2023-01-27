import pandas as pd


class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def filter_data(self, df, column, criteria):
        df_select = df[column] == criteria
        df_new = df[df_select]
        df_new.index = range(df_new.shape[0])
        return df_new

    def excluding_specific_charac(self, df, columns, charac_to_exclude):
        # Excluding specific non-numeric characters in every column of the list
        for column in columns:
            try:    
                df[column] = df[column].str.replace(f"[{charac_to_exclude}]","")
            except:
                print(f"The column named: {column} don't contains non-numeric character.")
                continue
    
        return df

    def convert_column_to_numeric_type(self, df, columns, target_type):
        for column in columns:
            try:
                df[column] = pd.to_numeric(df[column], errors = 'coerce').astype(target_type)
                print(f"Column: {column} transformed in {target_type} type.")
            except:
                print(f"Column: {column} it's not in a correct format to transform in {target_type} type.")
                continue
    
        return df

    def apply_fillna_in_columns(self, df, columns):
        for column in columns:
            df[column] = df[column].fillna(0)

        return df
