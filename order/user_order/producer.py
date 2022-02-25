import pika
import json

params = pika.URLParameters('amqps://ocnuzhno:kbiUzrNfGBGOo3cSte7TpjXAROgOEFye@dingo.rmq.cloudamqp.com/ocnuzhno')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='boss', body=json.dumps(body), properties=properties)
    
    
    

