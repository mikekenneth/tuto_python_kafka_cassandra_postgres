from .load_config import get_conf
from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient, NewTopic

# Read configurations from ini file
CONFIG = get_conf(ini_file=".conf.ini", section="KAFKA")
kafka_bootstrap_servers = f"{CONFIG['server']}:{CONFIG['port']}"

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {} --- MESSAGE: {}'.format(err, msg))

class Publish:
    def __init__(self, topics: list):
        """[summary]

        Args:
            topic (str): Spevify the topic to which
        """
        if self.create_topic_if_not_existing(topics=topics):
            self.topics = topics
            self.producer = Producer({
                'bootstrap.servers': kafka_bootstrap_servers
                })
        else:
            raise ValueError("Not able to create the topics")
            

    def publish_data(self, data: str):
        self.producer.poll(0)
        for topic in self.topics:
            self.producer.produce(topic, data.encode('utf-8'), callback=delivery_report)


    def create_topic_if_not_existing(self, topics:list):
        try:
            admin = AdminClient({'bootstrap.servers': kafka_bootstrap_servers})
            for topic in topics:
                if topic not in admin.list_topics().topics:
                    new_topic = NewTopic(topic, int(CONFIG['num_partitions']), int(CONFIG['num_replicas']))
                    admin.create_topics([new_topic,])
            return True
        except Exception:
            return False


    def __del__(self):
        self.producer.flush()


class Consume:
    def __init__(self, topics:list, group: str):
        self.topics = topics
        self.group = group
        self.consumer = Consumer({
            'bootstrap.servers': kafka_bootstrap_servers,
            'group.id': self.group,
            'auto.offset.reset': 'earliest'
            })
        self.consumer.subscribe(self.topics)

    def get_data(self):
        return self.consumer.poll(1.0)

    def __del__(self):
        self.consumer.close()
