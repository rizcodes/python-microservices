# Rabbit MQ service via cloudampq
# Consumer
import pika

params = pika.URLParameters('amqps://ejcumvmz:4aOsnI1mPEG33p9XCgFNxIAMaVK4Kij3@puffin.rmq2.cloudamqp.com/ejcumvmz')
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received event in ADMIN')
    print(f'--- {body} --')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()

channel.close()
