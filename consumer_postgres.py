from utils.kafka_manager import Consume
from utils.postgres_manager import Manager as Postgres_Manager
from utils.fake_data_generator import generate_profile, _get_columns

pg_manager = Postgres_Manager()

def process_data(data: str):
    cols = _get_columns('transactions_events')
    values = [d.strip() for d in data.decode("utf-8").split(',')]
    pg_manager.insert_single(tabname='f_transactions_events', cols=cols, values=values)
    

if __name__ == "__main__":
    topics = ["transactions_events"]
    consumer = Consume(topics=topics, group='group_1')
    try:
        while True:
            msg = consumer.get_data()
            if msg is None:
                print("Waiting for message or event/error in poll()")
                continue
            elif msg.error():
                print('Consumer Messages Error: {}'.format(msg.error()))
            else:
                process_data(msg.value())
    except KeyboardInterrupt:
        del(consumer)
