from kafka import KafkaProducer, KafkaConsumer

topic = 'my_kafka_topic'
bootstrap_servers = 'localhost:9093'
client_id = 'test'
api_version = (0, 10, 1)

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
