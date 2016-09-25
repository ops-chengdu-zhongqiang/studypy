#!/usr/bin/env python
#coding: utf-8

'''
Created on 2016年9月25日

@author:  ttxsgoto

每个thread实例都有一个名称，它有一个默认值，也可以在创建时改变
'''
import threading
import time
import logging

"""
def worker():
    print threading.currentThread().getName(),'Starting'
    time.sleep(2)
    print threading.currentThread().getName(),'Exiting'

def my_service():
    print threading.currentThread().getName(),'Starting'
    time.sleep(3)
    print threading.currentThread().getName(),'Exiting'
"""
logging.basicConfig(
    level = logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',                
    )

def worker():
    logging.debug("Starting")
    time.sleep(2)
    logging.debug("Exitingxxx")
def my_service():
    logging.debug("Starting")
    time.sleep(3)
    logging.debug("Exiting")


t = threading.Thread(name='my_service',target=my_service)
w = threading.Thread(name='worker',target=worker)
w2 = threading.Thread(target=worker)

w.start()
w2.start()
t.start()
