import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')
#如果输入的有值，就等于输入的，否则就等于info
severity = sys.argv[1] if len(sys.argv) >1 else 'info'

message = ''.join(sys.argv[2:]) or 'hello world'

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r:%r" % (severity, message))

connection.close()