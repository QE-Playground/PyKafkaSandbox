from kafka import KafkaAdminClient, KafkaConsumer
from kafka.admin import NewTopic

from src.libs.Singleton import Singleton
from src.utils.Logger import Logger


class Kafka(object, metaclass=Singleton):
    bootstrap_servers = 'localhost:9093'
    client_id = 'test'
    api_version = (0, 10, 1)

    def __init_(self, bootstrap_servers, client_id, api_version):
        self.bootstrap_servers = bootstrap_servers
        self.client_id = client_id
        self.api_version = api_version

    def create_topic(self, topic_name):
        """
        Create topic
        :param topic_name:
        :return:
        """
        admin_client = KafkaAdminClient(
            bootstrap_servers=self.bootstrap_servers,
            client_id=self.client_id,
            api_version=self.api_version
        )

        topic_list = [NewTopic(name=topic_name, num_partitions=1, replication_factor=1)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)

    def topic_exists(self, topic_name):
        consumer = KafkaConsumer(bootstrap_servers=self.bootstrap_servers)
        available_topics = consumer.topics()
        logger = Logger()
        logger.log.info(f'Available topics: {available_topics}')
        return topic_name in available_topics
