#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年4月29日

@author: zhongqiang

Describe: thread_event
'''
from threading import Thread,Event
from Queue import Queue
import time


que = Queue(maxsize=100)  #队列大小，先进先出，线程安全

def producer():
    print u"等人过来买包子。。。"
    event.wait()
    event.clear()  #将set标示位清空，设置为false
    
    print u"有人过来买包子了，哈哈。。。"
    print u"开始制作包子。。。"
    time.sleep(5)
    print u"你的包子准备好了 。。。"
    event.set()
    
def consumer():
    print u"消费者去购买包子"
    event.set()
    
    time.sleep(2)
    print u"等待去取包子"
    #event.wait()
    while True:
        if event.isSet():
            print u"包子好吃，结束"
            break
        else:
            print u"还没有准备好"
            time.sleep(1)
     
 
event = Event()

p = Thread(target=producer)
c = Thread(target=consumer)

p.start()
c.start()
 
 
 
 
 
 
 
 
    
