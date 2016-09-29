#!/usr/bin/env python
#coding: utf-8

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

#表示谁来获取，不再按照奇偶数 排列
channel.basic_qos(prefetch_count=1)

#从队列中取消息
channel.basic_consume(callback,
					queue="name2",
					no_ack=False)	#如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
