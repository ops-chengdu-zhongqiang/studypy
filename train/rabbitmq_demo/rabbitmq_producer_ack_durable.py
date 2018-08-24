#!/usr/bin/env python
# coding: utf-8
# 消息队列是可以做持久化，如果我们在生产消息的时候就指定某条消息需要做持久化，那么RabbitMQ发现有问题时，就会将消息保存到硬盘，持久化下来
# 此时rabbitmq down掉时，再启动 队列和数据也都是存在的，如果不持久化，down掉后队列就没有了

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

# 通过频道创建队列，如果有则忽略，没有则创建,指定队列持久化
channel.queue_declare(queue="name2", durable=True)

# 设置指定队列名称，body往队列中发送消息
channel.basic_publish(exchange='',
                      routing_key="name2",
                      ody="Hello World!",
                      properties=pika.BasicProperties(delivery_mode=2, ))  # 指定消息持久化

print " Sent 'Hello World!' "

# 关闭连接
connection.close()
