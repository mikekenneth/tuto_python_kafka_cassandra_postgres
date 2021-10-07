from utils.cassandra_manager import Manager as Cassandra_Manager
from utils.postgres_manager import Manager as Postgres_Manager

# Create cassandra keyspace and tables
# def create_cassandra_table():
#     with open('assets/schema/cassandra_createall.sql') as f:
#         queries = f.read()
#         manager = Cassandra_Manager(keyspace='tutorial_python_ks')
#         manager.execute(queries)

# Create postgres tables
def create_postgres_table():
    with open('assets/schema/postgres_createall.sql') as f:
        queries = f.read()
        manager = Postgres_Manager()
        manager.execute(queries)

if __name__ == "__main__":
    create_postgres_table()