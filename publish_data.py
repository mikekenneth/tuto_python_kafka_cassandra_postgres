from time import sleep
from utils.kafka_manager import Publish, topic
from utils.fake_data_generator import generate_transaction_data

number_of_transactions = 10**2  # I usually use this as
batch_size = 10
batch_interval = 1  # Number of seconds to sleep for each batch

counter = None
publisher = Publish(topic=topic)

for _ in range(number_of_transactions):
    if counter is None or counter == batch_size:
        counter = 0
        sleep(batch_interval)
    data = generate_transaction_data()
    publisher.publish_data(data=str(data))
    counter += 1
