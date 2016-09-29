#!/usr/bin/env python
#coding: utf-8
#exchange type = direct：任何发送到Direct Exchange的消息都会被转发到RouteKey中指定的Queue上(关键字发送)
#队列绑定关键字，发送者将数据关键字发送到消息Exchange，Exchange根据关键字判定应该将数据发送至指定队列
# 结论：当我们将发布者的key设置成Error的时候两个队列对可以收到Exchange的消息，当我们将key设置成info后，只有订阅者1可以收到Exchange的消息

import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",port=5672))

#创建一个频道
channel = connection.channel()

#指定exchange和对应的类型
channel.exchange_declare(exchange="test_direct",
					  type='direct')

typeinfo='error'
#设置exchange，没有指定routing_key，队列指定关键字
channel.basic_publish(exchange='test_direct',routing_key=typeinfo,body="Hello Chengdu!")

print " Sent routing_key:%s ——> body:'Hello Chengdu!' " %typeinfo

#关闭连接
connection.close() 
