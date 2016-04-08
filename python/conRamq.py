#coding=utf-8
import pika

def openChannel(channel):
    #Build connection and channel
    userName, pwd, ip, port='guest', 'guest', '54.84.57.116', 8443
    credentials=pika.PlainCredentials(userName, pwd)
    parameters=pika.ConnectionParameters(ip, port,'/', credentials)
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()

def openQueue(channel,queue):
    queue='esp.automationx.request.queue'
    channel.queue_declare(queue)
    print "Open queue"+queue+": OK"

def readBody(body):
    #Here to define a function to read body from meta files in local drive.
    body='test'

def pubMsg(body,channel):
    exchange,routing_key='', 'hello'
    channel.basic_pulish(exchange,routing_key,body)
    print "Publish done"

def close(connection):
    connection.close()

if __name__ == '__main__':
    print "Start connection..."
    userName, pwd, ip, port='guest', 'guest', '54.84.57.116', 8443
    credentials=pika.PlainCredentials(userName, pwd)
    parameters=pika.ConnectionParameters(ip, port,'/', credentials)
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
   # openChannel()
 #   openQueue(channel,queue)
#    readBody(body)
 #   pubMsg(body,channel)
  #  close(connection)
