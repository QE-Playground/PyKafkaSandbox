from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

topic = 'my_kafka_topic'
bootstrap_servers = 'localhost:9092'
client_id = 'test'
api_version = (0, 10, 1)

admin_client = KafkaAdminClient(
    bootstrap_servers=bootstrap_servers,
    client_id=client_id,
    api_version=api_version
)

topic_list = [NewTopic(name=topic, num_partitions=1, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    api_version=api_version,
    value_serializer=str.encode
)

producer.send(
    topic=topic,
    value='some_message_bytes'
)

producer.close()


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    api_version=api_version
)

for msg in consumer:
    print(msg)
