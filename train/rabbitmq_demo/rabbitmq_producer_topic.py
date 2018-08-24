#!/usr/bin/env python
# coding: utf-8
# exchange type = topic：任何发送到Topic Exchange的消息都会被转发到所有关心RouteKey中指定话题的Queue上(模糊匹配)
# 在topic类型下，可以让队列绑定几个模糊的关键字，之后发送者将数据发送到exchange，exchange将传入"路由值"和"关键字"进行匹配，匹配成功，则将数据发送到指定队列
# # ：表示可以匹配0个或多个单词
# * ：表示只能匹配一个单词

import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

# 指定exchange和对应的类型
channel.exchange_declare(exchange="test_topic", type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous'
message = ''.join(sys.argv[2:]) or 'Hello Chengdu!'

# 设置exchange，没有指定routing_key，队列指定关键字
channel.basic_publish(exchange='test_topic', routing_key=routing_key, body=message)

print " Sent routing_key:%s ——> body:%s " % (routing_key, message)

# 关闭连接
connection.close()
