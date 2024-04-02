import mysql.connector


class sql_proxy:
    def __init__(self, _host="localhost", _username="root", _password="", _database="sainbase"):
        self.mydb = mysql.connector.connect(
            host=_host,
            username=_username,
            password=_password,
            database=_database,
        )

    def close_connection(self):
        self.mydb.close()


    def get_tables(self):
        with self.mydb.cursor(buffered=True) as cursor:
            result = cursor.execute("SHOW TABLES")
            tables = [i[0] for i in cursor.fetchall()]
            return tables

    def get_table_columns(self,table):
        with self.mydb.cursor(buffered=True) as cursor:
            result = cursor.execute("SELECT * FROM " + table + " LIMIT 0")
            return cursor.column_names