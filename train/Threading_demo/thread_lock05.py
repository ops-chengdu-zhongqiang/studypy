#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年4月30日

@author: zhongqiang

Describe: 线程锁
'''

import threading
import time
from CodeWarrior.CodeWarrior_suite import target

num = 0


def run(n):
    time.sleep(1)
    global num
    # print "----%s" %lock.locked()
    lock.acquire()
    print lock.locked()
    time.sleep(0.001)
    num += 1
    lock.release()
    # time.sleep(0.1)
    print lock.locked()
    print '\n %d' % num


# lock = threading.Lock() #线程锁定义
# lock.acquire() #获取锁，开始独占cpu
# slock.release() #释放锁，可以被其他使用cpu资源
# slock.locked()  #主程序判断locked()状态
# lock = threading.RLock() #多把锁时引用，释放时也应该释放对应的多把锁
# lock = threading.BoundedSemaphore(4) #同时允许多少个线程进行数据修改


# for i in range(10):
#     t = threading.Thread(target=run,args=(i,))
#     t.start()


data = 0
lock = threading.Lock()  # 定义锁


def func():
    global data
    print "%s acquire lock ..." % threading.currentThread().getName()

    # print "acquire-----%s" %lock.acquire()
    if lock.acquire():  # 调用锁，返回是否获得锁
        print "%s get the lock." % threading.currentThread().getName()
        data += 1
        print data
        time.sleep(2)
        print "%s release lock..." % threading.currentThread().getName()

        lock.release()  # 调用release()将释放锁


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)

t1.start()
t2.start()
t3.start()
