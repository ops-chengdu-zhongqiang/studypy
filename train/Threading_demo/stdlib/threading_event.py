#!/usr/bin/env python
# coding: utf-8

'''
Created on 2016年9月25日

@author:  ttxsgoto
事件对象是实现线程间安全通信的一种简单方式，event管理一个内部标志，
调用者可以用set()和clear()方法控制这个标志，其他线程可以使用wait()暂停，
直到设置这个标志，其效果就是在允许继续之前阻塞线程的运行
'''
import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)


def wait_for_event(e):
    logging.debug("wait_for_event staring")
    event_is_set = e.wait()
    logging.debug("event set: %s ", event_is_set)


def wait_for_event_timeout(e, t):
    while not e.isSet():
        logging.debug("wait_for_event_timeout starting")
        event_is_set = e.wait()
        logging.debug('event set :%s', event_is_set)
        if event_is_set:
            logging.debug("processing event")
        else:
            logging.debug("doing other work")


e = threading.Event()
t1 = threading.Thread(name='block',
                      target=wait_for_event,
                      args=(e,)
                      )
t1.start()

t2 = threading.Thread(name="non_block",
                      target=wait_for_event_timeout,
                      args=(e, 2)
                      )
t2.start()

logging.debug("waiting before calling Event.set()")
time.sleep(3)
e.set()
logging.debug("Event is set")
