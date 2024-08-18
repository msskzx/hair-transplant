from confluent_kafka import Consumer, KafkaError
import os

def consume_messages():
    # TODO Celery, or apache Flink
    consumer = Consumer({
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
        'auto.offset.reset': 'earliest',
    })
    
    topic = os.getenv('KAFKA_TOPIC')
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break

            print(f"Received message: {msg.value().decode('utf-8')}")
            # TODO store

    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()
