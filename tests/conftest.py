from kafka import KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

from utils.Logger import Logger

bootstrap_servers = 'localhost:9093'
client_id = 'test'
api_version = (0, 10, 1)


def create_topic(topic_name):
    """
    Create topic
    :param topic_name:
    :return:
    """
    admin_client = KafkaAdminClient(
        bootstrap_servers=bootstrap_servers,
        client_id=client_id,
        api_version=api_version
    )

    topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
    admin_client.create_topics(new_topics=topic_list, validate_only=False)


def topic_exists(topic_name):
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    available_topics = consumer.topics()
    logger = Logger()
    logger.log.info(f'Available topics: {available_topics}')
    return topic_name in available_topics
