#!/usr/bin/env python
# coding: utf-8
# exchange type = fanout ：任何发送到Fanout Exchange的消息都会被转发到与该Exchange绑定(Binding)的所有Queue上

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

channel.exchange_declare(exchange="test_fanout",  # 创建一个exchange
                         type="fanout")  # 任何发送到fanout exchange的消息都会被转发到和exchange绑定的queue上

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 绑定，exchange绑定后端队列
channel.queue_bind(exchange="test_fanout",
                   queue=queue_name)

print "======================="


def callback(ch, method, properties, body):
    print "Received %s" % body


# 从队列中取消息
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)  # 如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
