
class Transform():
    def __init__(self):
        print("Instance of transform object\n")

    def exclude_character_in_columns(self, df, columns, characters):
        for column in columns:
            for character in characters:    
                df[column] = df[column].str.replace(character, "")

        return df

    def transform_columns_type(self, df, columns, target_type):
        for column in columns:
            try:
                df[column] = df[column].astype(target_type)
                print(f"Column: {column} transformed in {target_type} type.")
            except:
                print(f"Column: {column} it's not in a correct format to transform in {target_type} type.")
                continue
        return df


    