import psycopg2
from .load_config import get_conf

# Get Configurations
CONFIG = get_conf(ini_file=".conf.ini", section="POSTGRES")

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
    
    def __del__(self):
        self.cursor.close()
        self.conn.commit()