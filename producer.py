import json
import pika

params = pika.URLParameters('amqps://zobyksdf:tEXN4vKXrQskmY9Lmi39zqk5IcdHzkSE@kangaroo.rmq.cloudamqp.com/zobyksdf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
