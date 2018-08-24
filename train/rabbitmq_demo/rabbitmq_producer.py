#!/usr/bin/env python
# coding: utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

# 通过频道创建队列，如果有则忽略，没有则创建
channel.queue_declare(queue="name1")

# 设置指定队列名称，body往队列中发送消息
channel.basic_publish(exchange='', routing_key="name1", body="Hello World!")

print " Sent 'Hello World!' "

# 关闭连接
connection.close()
