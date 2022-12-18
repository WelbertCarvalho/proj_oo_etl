

class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def exclude_character_in_column(self, df, columns, character):
        for column in columns:
            df[column] = df[column].str.replace(character, "")
        return df
        