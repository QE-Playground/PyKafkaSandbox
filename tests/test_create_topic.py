import datetime

from tests.conftest import is_topic_exist, create_topic

topic = 'my_kafka_topic'


def test_create_topic():
    if not is_topic_exist(topic):
        create_topic(topic)

    assert is_topic_exist(topic)


def test_create_topic_with_random_name():
    timestamp = int(datetime.datetime.now().timestamp())
    random_topic = f'{topic}_{timestamp}'

    create_topic(random_topic)
    assert is_topic_exist(random_topic)
