import psycopg2
from typing import Union
from .load_config import get_conf

# Get Configurations
CONFIG = get_conf(ini_file=".conf.ini", section="POSTGRES")
_listOrTuple = Union[list, tuple]
class Manager:
    def __init__(self) -> None:
        """Initialize postgres database connection
        """
        self.conn = psycopg2.connect(
            host=CONFIG['server'],
            database=CONFIG['database'],
            user=CONFIG['username'],
            password=CONFIG['password']
        )
        self.cursor = self.conn.cursor()

    def execute(self, query: str):
        """Execute a query
        Args:
            query (str): Query to be executed
        """
        return self.cursor.execute(query)

    def insert_single(self, tabname:str, cols: _listOrTuple, values: _listOrTuple) -> str:
        values_formatted = ', '.join(f'{v}' for v in values)
        query = f"INSERT INTO {tabname} ({','.join(cols)}) VALUES {values_formatted}"
        return self.execute(query)
    
    def insert_multiple(self, tabname:str, cols: _listOrTuple, values_list: _listOrTuple) -> str:
        values_list_formmated = [', '.join(f'{v}' for v in values) for values in values_list]
        query = f"INSERT INTO {tabname} ({','.join(cols)}) VALUES {', '.join(f'{v}' for v in values_list_formmated)})"
        return self.execute(query)
    
    def __del__(self):
        self.cursor.close()
        self.conn.commit()