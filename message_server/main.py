import pika
from modules.messages import MessagesCollection
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, "/"))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

collection = MessagesCollection()

def on_request(ch, method, props, body):
    m = json.loads(body)
    collection.add(m)
    
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                     body=json.dumps(collection.response()))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()