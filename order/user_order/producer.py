import pika

params = pika.URLParameters('amqps://ocnuzhno:kbiUzrNfGBGOo3cSte7TpjXAROgOEFye@dingo.rmq.cloudamqp.com/ocnuzhno')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='boss', body='hello')
    

