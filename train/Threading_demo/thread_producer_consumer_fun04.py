#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年4月21日

@author: zhongqiang

Describe: 生产者消费者模式，函数式
1.解耦
2.支持并发：生产者把制造出来的数据往缓冲区一丢，就可以再去生产下一个数据，基不用依赖消费者的处理速度
3.支持忙闲不均

'''
import threading
import time, random
import Queue


def proudcer(name, que):
    while True:
        if que.qsize() < 3:
            que.put('生产包子')
            print "%s:生产了一个包子...." % name
        time.sleep(random.randrange(5))


def consumer(name, que):
    while True:
        try:
            que.get_nowait()  # 不等待队列是否有值
            print "%s:消费了一个包子...." % name
        except Exception:
            print u'没有包子可消费了 .....'
        time.sleep(random.randrange(3))


# 实例化生产者
q = Queue.Queue()
p1 = threading.Thread(target=proudcer, args=("生产者01", q))
p2 = threading.Thread(target=proudcer, args=("生产者02", q))
p1.start()
p2.start()

# 实例化消费者
c1 = threading.Thread(target=consumer, args=("消费者01", q))
c2 = threading.Thread(target=consumer, args=("消费者02", q))
c1.start()
c2.start()
"""

produce1 = None

con = threading.Condition()

def produce():
    global produce1
    
    if con.acquire():
        while True:
            if produce1 is None:
                print "produce ..."
                produce1 = "anything ---"
                
                con.notify()
            con.wait()
            time.sleep(2)

def consume():
    global produce1
    
    if con.acquire():
        while True:
            if produce1 is not None:
                print "consume ...."
                produce1 = None
                
                con.notify()
            
            con.wait()
            time.sleep(2)
    
t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)    
 
t2.start()   
t1.start()
"""
