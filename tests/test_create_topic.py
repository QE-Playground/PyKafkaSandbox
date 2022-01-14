import datetime

from src.libs.Kafka import Kafka

topic = 'my_kafka_topic'


def test_create_topic():
    kafka = Kafka()
    if not kafka.topic_exists(topic):
        kafka.create_topic(topic)

    assert kafka.topic_exists(topic)


def test_create_topic_with_random_name():
    timestamp = int(datetime.datetime.now().timestamp())
    random_topic = f'{topic}_{timestamp}'

    kafka = Kafka()
    kafka.create_topic(random_topic)
    assert kafka.topic_exists(random_topic)
