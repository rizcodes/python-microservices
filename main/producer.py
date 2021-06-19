# Rabbit MQ service via cloudampq
# Producer
import json
import pika

params = pika.URLParameters('amqps://ejcumvmz:4aOsnI1mPEG33p9XCgFNxIAMaVK4Kij3@puffin.rmq2.cloudamqp.com/ejcumvmz')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
