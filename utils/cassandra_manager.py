from cassandra.cluster import Cluster
from .load_config import get_conf

# Get Configurations
CONFIG = get_conf(ini_file=".conf.ini", section="CASSANDRA")

class Manager:
    def __init__(self, keyspace:str) -> None:
        """Initialize cassandra database connection

        Args:
            keyspace (str): Specify teh "KEYSPACE" that should be selected
        """
        self.cluster = Cluster([CONFIG['server']], port=CONFIG['port'])
        self.session = self.cluster.connect(keyspace)
    
    def execute(self, query: str):
        """Execute a query

        Args:
            query (str): Query to be executed
        """
        return self.session.execute(query)
    
    def __del__(self):
        self.cluster.shutdown()
        