#!/usr/bin/env python
#coding: utf-8
#消息队列是可以做持久化，如果我们在生产消息的时候就指定某条消息需要做持久化，那么RabbitMQ发现有问题时，就会将消息保存到硬盘，持久化下来

import time
import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port=5672))

#创建一个频道
channel = connection.channel()

#通过频道创建队列，如果有则忽略，没有则创建,队列持久化
channel.queue_declare(queue="name2",durable=True)

def callback(ch,method,properties,body):
	print "Received %s" %body  
	time.sleep(10)
	print "ok"
	ch.basic_ack(delivery_tag = method.delivery_tag) #向生产者发送消费完毕的确认消息，然后生产者将该条消息从队列中剔除

#从队列中取消息
channel.basic_consume(callback,
					queue="name2",
					no_ack=False)	#如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
