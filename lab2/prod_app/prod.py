import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('3.228.245.93', 5672, '/',
pika.PlainCredentials('user', 'password')))
channel = connection.channel()

sensor = "1"

print("Running Producer Application...")
while True:
  temp = random.uniform(12.0, 20.0)
  toReturn = sensor + " " + str(temp)

  channel.basic_publish(exchange='my_exchange', routing_key='test', body=toReturn)
  print(f'[x] Sent: {toReturn}')
  time.sleep(5)

connection.close()
