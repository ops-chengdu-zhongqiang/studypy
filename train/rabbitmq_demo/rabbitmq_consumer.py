#!/usr/bin/env python
# coding: utf-8

import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

# 通过频道创建队列，如果有则忽略，没有则创建
channel.queue_declare(queue="name1")


def callback(ch, method, properties, body):
    print "Received %s" % body


# 从队列中取消息
channel.basic_consume(callback,
                      queue="name1",
                      no_ack=True)  # 如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
