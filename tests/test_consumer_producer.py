import datetime

from src.libs.Kafka import Kafka

topic = 'my_kafka_topic'


def test_message_is_sent_successfully():
    timestamp = int(datetime.datetime.now().timestamp())
    random_topic = f'{topic}_{timestamp}'
    random_message = f'message_{timestamp}'
    binary_message = bytes(random_message, encoding='utf-8')

    kafka = Kafka()
    kafka.send_message(topic=random_topic, value=binary_message)
    assert kafka.message_is_sent_successfully(topic=random_topic, value=binary_message)

    # Teardown
    kafka.delete_all_topics()
    assert kafka.get_available_topics() == set()
