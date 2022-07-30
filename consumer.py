import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.exchange_declare(exchange='ex_mensagens', exchange_type='fanout')
channel.queue_declare(queue='cliente_ayslan', exclusive=True)
channel.queue_declare(queue='cliente_amanda', exclusive=True)
channel.queue_bind(exchange='ex_mensagens', queue='')



def callback(ch,method, properties, body):
    print(body)

channel.basic_consume(queue = 'cliente_ayslan',on_message_callback=callback, auto_ack=True)
channel.basic_consume(queue = 'cliente_amanda',on_message_callback=callback, auto_ack=True)

channel.start_consuming()