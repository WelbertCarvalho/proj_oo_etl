import pandas as pd


class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def transform_columns_type(self, df, columns, target_type):
        for column in columns:
            df[column] = df[column].str.extract('(\d+)', expand = False)
            try:
                df[column] = df[column].astype(target_type)
                print(f"Column: {column} transformed in {target_type} type.")
            except:
                print(f"Column: {column} it's not in a correct format to transform in {target_type} type.")
                continue
        return df

    def apply_fillna(self):
        pass

    def delete_where_nan(self):
        pass

    def group_data(self, df, col_to_group, col_to_analyze, function):
        if function == "count":
            group = df.groupby(col_to_group)[col_to_analyze].count()
        elif function == "sum":
            group = df.groupby(col_to_group)[col_to_analyze].sum()
        elif function == "mean":
            group = df.groupby(col_to_group)[col_to_analyze].mean()
        elif function == "median":
            group = df.groupby(col_to_group)[col_to_analyze].median()
        elif function == "min":
            group = df.groupby(col_to_group)[col_to_analyze].min()
        elif function == "max":
            group = df.groupby(col_to_group)[col_to_analyze].max()
        elif function == "mode":
            group = df.groupby(col_to_group)[col_to_analyze].mode()
        elif function == "std":
            group = df.groupby(col_to_group)[col_to_analyze].std()
        elif function == "var":
            group = df.groupby(col_to_group)[col_to_analyze].var()
        else:
            print("The function informed it's not suported. Please, check pandas doc for more information about acceptable functions to use within groupby")
            return None

        group = pd.DataFrame(group, columns = [col_to_analyze])

        group = group.sort_values(by=[col_to_analyze], ascending = False)
        print(type(group))

        return group

    def filter_data(self, df, column, criteria):
        df_select = df[column] == criteria
        df = df [df_select]
        return df

    def df_total_rows(self, df):
        count_rows = df.shape[0]
        return f'Number of rows: {count_rows}'
