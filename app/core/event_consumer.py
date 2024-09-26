from kafka import KafkaConsumer
import json
from app.core.config import KAFKA_BOOTSTRAP_SERVERS

# Kafka consumer instance
consumer = KafkaConsumer(
    'account_created',
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    group_id='my-group'
)

def consume_event():
    for message in consumer:
        event_data = json.loads(message.value)
        print(f"Consumed event: {event_data}")
