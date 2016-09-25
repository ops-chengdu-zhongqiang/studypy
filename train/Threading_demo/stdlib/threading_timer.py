#!/usr/bin/env python
#coding: utf-8

'''
Created on 2016年9月25日

@author:  ttxsgoto
Timer在一个延迟之后开始工作，可以在这个延迟期间内的任意时刻取消
'''

import threading
import logging
import time

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s)  %(message)s',
    )

def delayed():
    logging.debug("worker running")
    return

t1 = threading.Timer(3,delayed)
t1.setName('t1')
t2 = threading.Timer(3,delayed)
t2.setName('t2')

logging.debug("starting timers")
t1.start()
t2.start()

logging.debug("Waiting before canceling %s",t2.getName())
time.sleep(2)
logging.debug('canceling %s', t2.getName())
t2.cancel()

logging.debug("done")
