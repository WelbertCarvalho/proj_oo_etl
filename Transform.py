

class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def replace_specific_characters(self, df, column_name):
        df[column_name] = df[column_name].replace("$", "")
        return df
        