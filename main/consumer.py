# Rabbit MQ service via cloudampq
# Consumer
import pika
import json
import logging
import logging.config
import yaml

from main import Dinosaur, db

# Logger
with open('logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

# RabbitMQ param
params = pika.URLParameters('amqps://ejcumvmz:4aOsnI1mPEG33p9XCgFNxIAMaVK4Kij3@puffin.rmq2.cloudamqp.com/ejcumvmz')

# Set ampq connection vis pika
connection = pika.BlockingConnection(params)

# Channel setup
channel = connection.channel()
channel.queue_declare(queue='main')


# Event caller
def callback(ch, method, properties, body):
    data = json.loads(body)
    logger.debug(f'AppMain: {data}')

    if properties.content_type == 'created':
        dinosaur = Dinosaur(id=data.get('id', 'null'), name=data.get('name', 'null'),
                            image=data.get('image', 'null'))
        db.session.add(dinosaur)
        db.session.commit()
        logger.debug(f'Dinosaur [{data["name"]}] added in DB')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)
logger.debug('Started Consumer')
channel.start_consuming()

channel.close()
