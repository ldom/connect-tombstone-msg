import json

from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError


def connector_name_from_key(key):
    # what we get: key = b'["test-source", {"filename": "/tmp/test.txt"}]'
    key_obj = json.loads(key)
    for item in key_obj:
        # we return the first item that is a string (JSON loads doesn't guarantee the ordering of the parsed object)
        if isinstance(item, str):
            return item
    return None


def create_tombstone_msg(kafka_url, connector_name, offset_storage_topic):
    print(f"create_tombstone_msg({kafka_url}, {connector_name}, {offset_storage_topic})")

    # it'd be nice to get the offset_storage_topic name programmatically
    # but it doesn't seem to be possible using the Connect REST API

    # read the last message for the connector
    consumer = KafkaConsumer(offset_storage_topic,
                             bootstrap_servers=kafka_url,
                             auto_offset_reset='earliest',
                             enable_auto_commit=False,
                             consumer_timeout_ms=100,
                             )
    latest_msg_partition = None
    message_key = None

    for message in consumer:
        if connector_name_from_key(message.key) == connector_name:
            latest_msg_partition = message.partition
            message_key = message.key

    # write a null tombstone msg to the proper broker
    producer = KafkaProducer(bootstrap_servers=kafka_url)
    future = producer.send(offset_storage_topic, key=message_key, value=None, partition=latest_msg_partition)

    TIMEOUT = 10
    try:
        future.get(timeout=TIMEOUT)
    except KafkaError:
        raise RuntimeError(f"Failed to write tombstone message within the imparted time ({TIMEOUT}s)")

    print("Done.")
