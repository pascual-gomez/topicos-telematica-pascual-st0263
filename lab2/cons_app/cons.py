import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('3.228.245.93', 5672, '/',
pika.PlainCredentials("user", "password")))
channel = connection.channel()

def callback(ch, method, properties, body):
        answer = body.decode("utf-8").split()
        sensor = answer[0]
        temperature = answer[1]
        print('###########################')
        print(f'{temperature} is received by sensor {sensor}')

        if float(temperature) < 15.0:
                print('temperature is too low. If on, air conditioner will be turned off.')
        elif float(temperature) > 18.0:
                print('temperature is too high. If off, air conditioner will be turned on.')
        else:
                print('temperature is ok')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
channel.start_consuming()
