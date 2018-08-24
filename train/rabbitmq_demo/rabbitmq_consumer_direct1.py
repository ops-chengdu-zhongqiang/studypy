#!/usr/bin/env python
# coding: utf-8
# exchange type = direct：任何发送到Direct Exchange的消息都会被转发到RouteKey中指定的Queue上(关键字发送)
# 队列绑定关键字，发送者将数据关键字发送到消息Exchange，Exchange根据关键字判定应该将数据发送至指定队列

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1", port=5672))

# 创建一个频道
channel = connection.channel()

channel.exchange_declare(exchange="test_direct",  # 创建一个exchange
                         type="direct")

# 随机创建队列
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

typeinfo = ['error', 'info', ]
# 绑定，exchange绑定后端队列
for type1 in typeinfo:
    channel.queue_bind(exchange="test_direct", queue=queue_name, routing_key=type1)

print "======================="


def callback(ch, method, properties, body):
    print "Received %s -----%s " % (method.routing_key, body)


# 从队列中取消息
channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)  # 如果no_ack=False,当消费者down掉，rabbitmq会重新将该任务添加到队列中

print "Waiting for messages,To exit press CTRL + C"
channel.start_consuming()
