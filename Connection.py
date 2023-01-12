import mysql.connector
from sqlalchemy import create_engine

from config import connections as c


class Connection:
    def __init__(self):
        print("Instance of connection object\n")

    def mysql_con(self, database_name):
        try:
            con = mysql.connector.connect(
                host = c[database_name]["host"],
                database = c[database_name]["database"],
                user = c[database_name]["user"],
                password = c[database_name]["password"]
            )
            print(f"Database: {c[database_name]['database']}\nUser: {c[database_name]['user']}\n")
            return con
        except:
            print(f"It was not possible to connect to {c[database_name]['database']}. Verify your connection.\n")
            return None

    def sqlalchemy_conn(self, database_name, type_connection):
        user = c[database_name]["user"]
        password = c[database_name]["password"]
        host = c[database_name]["host"]
        port = c[database_name]["port"]
        database = c[database_name]["database"]

        con = create_engine(
            url = f"{type_connection}://{user}:{password}@{host}:{port}/{database}"
        )
        print(f"Connection stablished: {database_name}")

        return con