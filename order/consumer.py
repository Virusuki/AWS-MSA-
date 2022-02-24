import pika

params = pika.URLParameters('amqps://ocnuzhno:kbiUzrNfGBGOo3cSte7TpjXAROgOEFye@dingo.rmq.cloudamqp.com/ocnuzhno')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='order')

def callback(ch, method, properties, body):
    print('Received in order')
    print(body)
    
channel.basic_consume(queue='order', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()
