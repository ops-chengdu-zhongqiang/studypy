#!/usr/bin/env python
#coding: utf-8
#exchange type = topic：任何发送到Topic Exchange的消息都会被转发到所有关心RouteKey中指定话题的Queue上(模糊匹配)
#在topic类型下，可以让队列绑定几个模糊的关键字，之后发送者将数据发送到exchange，exchange将传入"路由值"和"关键字"进行匹配，匹配成功，则将数据发送到指定队列

import sys
import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port=5672))

#创建一个频道
channel = connection.channel()

#创建一个exchange,并指定类型
channel.exchange_declare(exchange="test_topic",	
					type="topic")

#随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


binding_keys=sys.argv[1:]

if not binding_keys:
	sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
	sys.exit(0)


for binding_key in binding_keys:
	channel.queue_bind(exchange="test_topic",queue=queue_name,routing_key=binding_key)	

print "======================="

def callback(ch,method,properties,body):
	print "Received %s -----%s " %(method.routing_key,body)  
	
#从队列中取消息
channel.basic_consume(callback,
					queue=queue_name,
					no_ack=True)	#如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
