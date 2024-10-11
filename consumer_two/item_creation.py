import pika
import json
import time

def connect_to_rabbitmq():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Connection failed, retrying in 5 seconds... Error: {e}")
            time.sleep(5)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Item Creation Consumer received: {data}")
    # Add code here to insert data into the database

def consume_messages():
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='inventory_updates')
    channel.basic_consume(queue='inventory_updates', on_message_callback=callback, auto_ack=True)
    print('Waiting for item creation messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
