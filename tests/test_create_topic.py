import datetime

from tests.conftest import topic_exists, create_topic

topic = 'my_kafka_topic'


def test_create_topic():
    if not topic_exists(topic):
        create_topic(topic)

    assert topic_exists(topic)


def test_create_topic_with_random_name():
    timestamp = int(datetime.datetime.now().timestamp())
    random_topic = f'{topic}_{timestamp}'

    create_topic(random_topic)
    assert topic_exists(random_topic)
