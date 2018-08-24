#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年4月25日

@author: zhongqiang

Describe: 多线程的实现方式和相关的方法
'''

from threading import Thread
from time import sleep, ctime, sleep


def myfunction(arg):
    for item in range(10):
        print item
        sleep(1)


print "before"
t1 = Thread(target=myfunction, args=('hello',))
print t1.getName()  # Thread-1
print t1.isDaemon()  # 默认为false
# t1.setDaemon(True)  #设置为setDaemon模式

t1.start()
t1.join(timeout=5)

print "after"
print "Over"

sleep(5)
