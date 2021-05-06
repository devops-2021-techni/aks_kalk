from flask import Flask
import pika, uuid, json


app = Flask(__name__)

def addition(Number1, Number2):
    return Number1 + Number2

class GetMessage(object):

    def __init__(self):
        self.params = pika.URLParameters('amqps://ihlzrxjn:zidQ4Z8wUFList1uiLw6IA19vWT4km8U@rat.rmq2.cloudamqp.com/ihlzrxjn')

        self.connection = pika.BlockingConnection(self.params)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, channel, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, numbers_additions_json):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=numbers_additions_json)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

@app.route('/')
def index():

    return "Dernier resultat : test update bis "

@app.route('/hello/<prenom>/<nom>')
def hello(prenom,nom):
    SayHello = GetMessage()

        
    data_to_convert={"firstname": prenom, "surname": nom}

    terms_additions_json_to_send = json.dumps(data_to_convert)


    result = SayHello.call(terms_additions_json_to_send)

    return result


    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
