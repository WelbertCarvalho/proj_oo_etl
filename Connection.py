import mysql.connector
import config as c

class Connection:
    def __init__(self):
        print("Instance of connection object\n")

    def mysql_datalake_con(self):
        try:
            con = mysql.connector.connect(
                host = c.datalake_host,
                database = c.datalake_database,
                user = c.datalake_user,
                password = c.datalake_password
            )
            print(f"Database: {c.datalake_database}\nUser: {c.datalake_user}\n")
            return con
        except:
            print(f"It was not possible to connect to {c.datalake_database}. Verify your connection.\n")
            return None

    def mysql_datawarehouse_con(self):
        try:
            con = mysql.connector.connect(
                host = c.data_warehouse_host,
                database = c.data_warehouse_database,
                user = c.data_warehouse_user,
                password = c.data_warehouse_password
            )
            print(f"Database: {c.datalake_database}\nUser: {c.datalake_user}\n")
            return con
        except:
            print(f"It was not possible to connect to {c.data_warehouse_database}. Verify your connection.\n")
            return None