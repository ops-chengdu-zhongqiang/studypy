#!/usr/bin/env python
# coding: utf-8

'''
Created on 2016年9月25日

@author:  ttxsgoto
enumerate()会返回活动Thread实例的一个列表，这个列表也包括当前线程，由于等待当前线程结束会引入一种死锁状态，
所以必须将其跳过
'''
import random
import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s)  %(message)s',
)


def worker():
    t = threading.currentThread()
    pause = random.randint(1, 5)
    logging.debug("sleeping %s", pause)
    time.sleep(pause)
    logging.debug("Ending")
    return


for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
print "main_thread: ----%s" % main_thread
for t in threading.enumerate():
    print t
    if t is main_thread:
        continue
    logging.debug("Joining %s", t.getName())
    t.join()
