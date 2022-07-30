import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

mensagem = 'Oi pessoal!'
channel.exchange_declare(exchange='ex_mensagens', exchange_type='fanout')
channel.basic_publish(exchange='ex_mensagens', body=mensagem, routing_key='')
connection.close()