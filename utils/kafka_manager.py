from load_config import get_conf
from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

# Read configurations from ini file
CONFIG = get_conf(ini_file=".config.ini", section="KAFKA")

kafka_bootstrap_servers = f"{CONFIG['SERVER']}:{CONFIG['PORT']}"
topic = CONFIG['TOPIC']

# If topic not existing, create the topics
admin = AdminClient({'bootstrap.servers': kafka_bootstrap_servers})
if topic not in admin.list_topics().topics:
    new_topic = NewTopic(topic, int(CONFIG['NUM_PARTITIONS']), int(CONFIG['NUM_REPLICAS']))
    admin.create_topics([new_topic,])


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {} --- MESSAGE: {}'.format(err, msg))

class Publish:
    def __init__(self, topic):
        self.topic = topic
        self.producer = Producer({
            'bootstrap.servers': kafka_bootstrap_servers
            })

    def publish_data(self, data: str):
        self.producer.poll(0)
        self.producer.produce(self.topic, data.encode('utf-8'), callback=delivery_report)

    def __del__(self):
        self.producer.flush()


class Consume:
    def __init__(self, topic, group):
        self.topic = topic
        self.group = group
        self.consumer = Consumer({
            'bootstrap.servers': kafka_bootstrap_servers,
            'group.id': self.group,
            'auto.offset.reset': 'earliest'
            })
        self.consumer.subscribe([self.topic])

    def get_data(self):
        return self.consumer.poll(1.0)

    def __del__(self):
        self.consumer.close()
