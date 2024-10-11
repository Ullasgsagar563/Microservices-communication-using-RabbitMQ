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

def publish_message(message):
    connection = connect_to_rabbitmq()
    channel = connection.channel()
    channel.queue_declare(queue='inventory_updates')
    channel.basic_publish(exchange='', routing_key='inventory_updates', body=json.dumps(message))
    print(f"Published message: {message}")
    connection.close()

if __name__ == "__main__":
    while True:
        message = {"item": "item_name", "quantity": 10}
        publish_message(message)
        time.sleep(5)
