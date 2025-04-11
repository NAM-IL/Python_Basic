import sqlite3

class DbHandler():
    """
    _summary_
    """

    def __init__(self):
        self.query = """
        CREATE TABLE test(a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);
        """

    def connect_db(self, db_full_name="mydata.db"):
        # conn = sqlite3.connect("mydata.db")
        conn = sqlite3.connect(db_full_name)
        conn.execute(self.query)
        conn.commit()