#!/usr/bin/env python
# coding: utf-8

'''
Created on 2016年9月25日

@author:  ttxsgoto
程序有时会创建一个线程作为守护线程(deamon)，这个线程可以一直运行而不阻塞主程序退出，
要标志一个线程为守护线程，需要调用setDeamon()方法并提供参数True,默认情况下线程不作为守护线程
要等待一个守护线程完成工作，需要使用join(s)方法，在这个s时间内没有完成，join()也会返回
'''
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


def deamon():
    logging.debug("Starting")
    time.sleep(2)
    logging.debug("Exiting")


def non_daemon():
    logging.debug("Starting")
    logging.debug("Exiting")


d = threading.Thread(name='deamon', target=deamon)
d.setDaemon(True)

w = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
w.start()

d.join(1)
print d.isAlive()
w.join()
