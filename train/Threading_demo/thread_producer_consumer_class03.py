#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年4月29日

@author: zhongqiang

Describe: Class ——生产者，消费者模型
'''
from threading import Thread
from Queue import Queue
import time

que = Queue(maxsize=100)  # 队列大小，先进先出，线程安全


class producer(Thread):
    def __init__(self, name, queue):
        """
        @param name:名字
        @param queue: 容器
        """
        self.__Name = name
        self.__Queue = queue
        super(producer, self).__init__()  # 执行父类的构造函数

    def run(self):  # 重写run方法
        while True:
            if self.__Queue.full():
                time.sleep(2)
            else:
                self.__Queue.put("生产包子")  # 存放
                time.sleep(1)
                print "%s 生产了一个包子" % self.__Name
                # Thread.run(self)


class consumer(Thread):
    def __init__(self, name, queue):
        """
        @param name:名字
        @param queue: 容器
        """
        self.__Name = name
        self.__Queue = queue
        super(consumer, self).__init__()  # 执行父类的构造函数

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(2)
            else:
                self.__Queue.get()  # 取出
                time.sleep(1)
                print "%s 消费了一个包子" % self.__Name
                # Thread.run(self)


# 实例化生产者
p1 = producer('生产者01', que)
p1.start()
p2 = producer('生产者02', que)
p2.start()
p3 = producer('生产者03', que)
p3.start()

# 实例化消费者
for item in range(20):
    name = "消费者%d" % item
    temp = consumer(name, que)
    temp.start()
