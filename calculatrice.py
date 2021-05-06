from flask import Flask, request
import pika, uuid, json


app = Flask(__name__)


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

    def on_response(self, _channel, _method, _properties, body):
        if self.corr_id == _properties.correlation_id:
            self.response = body

    def call(self, numbers_additions_json, _properties):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
                content_type=_properties
            ),
            body=numbers_additions_json)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

@app.route('/')
def index():


    return "result"

@app.route('/add/<int:add1>/<int:add2>')
def add(add1,add2):
    DoMath = GetMessage()

        
    data_to_convert={"term1": add1, "term2": add2}

    terms_additions_json_to_send = json.dumps(data_to_convert)


    result = DoMath.call(terms_additions_json_to_send,"do_addition")

    return result


@app.route('/history/')
def history():
    DoMath = GetMessage()

        
    data_to_convert={"term1": "2", "term2": "3"}

    terms_additions_json_to_send = json.dumps(data_to_convert)


    result = DoMath.call(terms_additions_json_to_send,"get_history")

    return result


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
