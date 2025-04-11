from sqlalchemy import create_engine
import pandas as pd

class SqlalchemyKlass:
    """_summary_
    """
    
    def __init__(self, dbfullpath):
        self.db = create_engine(f"sqlite:///{dbfullpath}")
        
    def read_db(self):
        """
            read db data

        Returns:
            _type_: _description_
        """
        print("read_db 함수")
        df = pd.read_sql("SELECT * from test", self.db)
        # print(f"df: {df.head()}")
        return df