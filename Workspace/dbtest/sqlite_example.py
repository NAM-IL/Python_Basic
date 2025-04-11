import sqlite3
import pandas as pd
import sqlalchemy as sqla

class DbHandler():
    """
    _summary_
    """

    def __init__(self):
        self.query = """
        CREATE TABLE test(a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);
        """

    def connect_db(self, db_full_name):
        """
            connect_db
        Args:
            db_full_name (_type_): _description_
        """

        print("connect_db 함수")

        # conn = sqlite3.connect("mydata.db")
        self.db_connection = sqlite3.connect(db_full_name)

        try:
            self.db_connection.execute(self.query)
            self.db_connection.commit()
        except Exception as ex:
            print(f"Exception: {ex}")

    def insert_db_data(self, stmt, data):
        """
        insert_db_data
        Args:
            stmt (_type_): _description_
            data (_type_): _description_
        """

        print("insert_db_data 함수")
        # print(f"stmt: {stmt}")
        try:
            self.db_connection.executemany(stmt, data)
            self.db_connection.commit()
        except Exception as ex:
            print(f"Exception: {ex}")

    def read_db_data(self):
        """
            read db test
        """
        cursor = self.db_connection.execute("SELECT * FROM test")
        rows = cursor.fetchall()
        # print(f"rows:\n{rows}")
        # print(f"description:\n{item[0]}")
        df = pd.DataFrame(data=rows, columns=[item[0] for item in cursor.description])

        return df

    def update_db_data(self):
        print("update_db_data 함수")

    def delete_db_data(self):
                print("delete_db_data 함수")