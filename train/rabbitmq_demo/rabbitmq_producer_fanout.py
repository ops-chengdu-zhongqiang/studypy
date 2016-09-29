#!/usr/bin/env python
#coding: utf-8
#exchange type = fanout ：任何发送到Fanout Exchange的消息都会被转发到与该Exchange绑定(Binding)的所有Queue上

import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port=5672))

#创建一个频道
channel = connection.channel()

#指定exchange和对应的类型
channel.exchange_declare(exchange="test_fanout",
					  type='fanout')

#设置exchange，没有指定routing_key，队列随机
channel.basic_publish(exchange='test_fanout',routing_key="",body="Hello Chengdu!")

print " Sent 'Hello Chengdu!' "

#关闭连接
connection.close() 
