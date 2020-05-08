# connect-tombstone-msg

CLI script + library to write a connector tombstone msg

https://rmoff.net/2019/08/15/reset-kafka-connect-source-connector-offsets/

```
usage: add_tombstone_msg.py [-h] [-o OFFSET_STORAGE_TOPIC] [-b BROKER]
                            connector

positional arguments:
  connector             Name of the connector to write a tombstone message for

optional arguments:
  -h, --help            show this help message and exit
  -o OFFSET_STORAGE_TOPIC, --offset-storage-topic OFFSET_STORAGE_TOPIC
                        Name of the topic storing the offsets for the
                        connector (defaults to 'connect-offsets')
  -b BROKER, --broker BROKER
                        Kafka Broker URL (defaults to 'localhost:9092')
  ```
