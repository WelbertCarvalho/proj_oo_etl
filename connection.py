from sqlalchemy import create_engine
from config import connections as c

class Connection:
    def __init__(self):
        print("Instance of connection object\n")

    def sqlalchemy_conn(self, database_name, type_connection):
        user = c[database_name]["user"]
        password = c[database_name]["password"]
        host = c[database_name]["host"]
        port = c[database_name]["port"]
        database = c[database_name]["database"]

        url = f"{type_connection}://{user}:{password}@{host}:{port}/{database}"

        con = create_engine(
            url = url
        )
        
        print(f"Connection stablished: {database_name}")

        return con
