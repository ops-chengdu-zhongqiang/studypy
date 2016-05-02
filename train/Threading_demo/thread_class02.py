#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年4月29日

@author: zhongqiang

Describe: 线程类
        1.在父类中init中有target,args定义
        2.执行start()方法后，等待cpu的调度
        3.将target的值和args的值传递给run函数执行
'''
from threading import Thread
import time

class mythread(Thread): #继承父类的threading.Thread
    def __init__(self,threadid,threadname,counter):
        Thread.__init__(self)
        self.threadid = threadid
        self.threadname = threadname
        self.counter = counter
        

    def run(self): #把要执行的代码写在run函数中，线程创建后会直接运行run函数
        print "Starting %s \n" %self.threadname
        
        print_time(self.name,self.counter,self.threadid)
        #Thread.run(self.threadname,self.threadid,5)
        
        print "Exiting %s" %self.threadname

def print_time(threadName,delay,counter):
    while counter :
        time.sleep(delay)
        print counter,"%s: %s" %(threadName,time.ctime())
        counter -=1

t1 = mythread(2,"线程一",1)
# t2 = mythread(2,"线程二",1)
# 
t1.run()
# t2.run()

print "Exiting Main Thread"


class MyThread(Thread):#继承thread
    
    def run(self): #重写run方法
        time.sleep(5)
        print "threading-------"
        #myfunction()
        Thread.run(self)  #执行父类的run方法


def myfunction():
    print "Myfunction"

# t1 = MyThread(target=myfunction) #执行从thread中继承来的__init__函数
# t1.start()
#   
# print "end------"










