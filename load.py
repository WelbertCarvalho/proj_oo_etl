from connection import Connection

class Load:
    def __init__(self):
        print("Instance of load object\n")

    def load_data_frame_in_sql_db(self, df, target_conn, type_connection, table_name):
        instance_connection = Connection()
        con = instance_connection.sqlalchemy_conn(
            database_name = target_conn, 
            type_connection = type_connection   
        )

        print(con)

        df.to_sql(
            name = table_name,
            con = con,
            if_exists = 'append'
        )

        return f"A table named {table_name} was created in the DB."
