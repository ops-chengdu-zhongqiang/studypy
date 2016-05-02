#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年4月24日

@author: zhongqiang

Describe: 多进程,进程间共享内存可通过Queue,Manager
'''

from multiprocessing import Pool,Process,Queue,Manager

import os

#方法一

def f(x):
    return x*x

"""
if __name__ == '__main__':
    p = Pool(5) #进程池，最多跑几个进程
    print (p.map(f, [1,2,3]))
"""

#多进程，父进程和子进程

def info(title):
    print title
    print "module name:",__name__
    if hasattr(os, 'getppid'): #only available on unix
        print "parent process:",os.getppid()
    print "process id:",os.getpid()

def f(name):
    info('function f')
    print 'hello',name
"""
if __name__ == '__main__':
    info('main line')
    print "------------"
    p = Process(target=f,args=('bob',))
    p.start()
    p.join()
#http://www.cnblogs.com/kaituorensheng/p/4445418.html
"""
"""
from multiprocessing import Process,Manager
import threading
import time
def run(info_list,n):
    info_list.append(n)
    print info_list

info=[]
for i in range(10):
    p = Process(target=run,args=(info,i))
    p.start()
    print p.pid
    print p.name
    print p.is_alive()
    

p = Process(target=run,args=(info,2))
p.start()

time.sleep(0.1)
print "Threading---------"
info2=[]
for i in range(10):
    p = threading.Thread(target=run,args=(info2,i))
    p.start()
    time.sleep(0.01)
    
manager = Manager()
d = manager.dict()

"""

#类继承方式

import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        print "Begin----"
        myfunction(self.interval)
        print "End-----"
        
def myfunction(ms):
    n = 5
    while n > 0:
        print("the time is %s" %format(time.ctime()))
        time.sleep(ms)
        n -= 1

if __name__ == '__main__':
    p = MyProcess(1)
    p.daemon = True  #当子进程设置了daemon属性时，主进程结束，子进程也随之结束
    p.start()
    time.sleep(3)
    print "Main Process is Over...."




    
    







