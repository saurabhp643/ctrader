from kafka import KafkaProducer
import json
from app.core.config import KAFKA_BOOTSTRAP_SERVERS

# Kafka producer instance
producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)

def produce_event(topic, event_data):
    # Convert event data to JSON and send to Kafka
    producer.send(topic, json.dumps(event_data).encode('utf-8'))
