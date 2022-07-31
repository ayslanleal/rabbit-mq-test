import pika


class BasicConsumer():
    def __init__(self,host, exchange):
        self.host = host
        self.exchange = exchange
        self.type = 'fanout'
        self.queue = ''

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()

    def on_queue_declare(self):
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.type)
        self.channel.queue_declare(queue='consumer_ayslan', exclusive=True)
        self.channel.queue_declare(queue='consumer_amanda', exclusive=True)
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue)


    def on_bindok(self,callback):
        self.start_publishing(callback)



    def start_publishing(self,callback):
        self.channel.basic_consume(
            queue='consumer_ayslan',
            on_message_callback=callback,
            auto_ack=True
        )

        self.channel.basic_consume(
            queue='consumer_amanda',
            on_message_callback=callback,
            auto_ack=True
        )

    def start_consum(self):
        self.channel.start_consuming()

if __name__ == '__main__':
    def callback(ch,method, properties,body):
        print(body)

    consumer = BasicConsumer('localhost','ex_mensagens')
    consumer.on_queue_declare()
    consumer.on_bindok(callback)
    consumer.start_consum()