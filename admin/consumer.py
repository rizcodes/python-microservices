# Rabbit MQ service via cloudampq
# Consumer
import os
import django
import pika
import json
import logging.config
import yaml

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()

from dinosaurs.models import Dinosaur

# Logger
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

params = pika.URLParameters('amqps://ejcumvmz:4aOsnI1mPEG33p9XCgFNxIAMaVK4Kij3@puffin.rmq2.cloudamqp.com/ejcumvmz')
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    data = json.loads(body)
    logger.debug(f'AppAdmin: {data}')

    if properties.content_type == 'liked':
        logger.debug('Received a like from main')
        dinosaur = Dinosaur.objects.get(id=data['id'])
        dinosaur.likes = data['likes']
        dinosaur.save()


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
logger.debug('Started Consuming')
channel.start_consuming()

channel.close()
