import argparse

from tombstone_msg import create_tombstone_msg


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("connector",
                        help="Name of the connector to write a tombstone message for")
    parser.add_argument("-o", "--offset-storage-topic",
                        help="Name of the topic storing the offsets for the connector (defaults to 'connect-offsets')",
                        default="connect-offsets")
    parser.add_argument("-b", "--broker",
                        help="Kafka Broker URL (defaults to 'localhost:9092')",
                        default="localhost:9092")
    # parser.add_argument("-c", "--connect",
    #                     help="Connect URL (defaults to 'localhost:8083')",
    #                     default="localhost:8083")

    args = parser.parse_args()

    return create_tombstone_msg(kafka_url=args.broker,
                                # connect_url=args.connect,
                                connector_name=args.connector,
                                offset_storage_topic=args.offset_storage_topic)

if __name__ == "__main__":
    main()

