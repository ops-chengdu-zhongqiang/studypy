#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/26

Describe: 
'''

from functools import wraps
import logging
import datetime, time


def logged(level, name=None, message=None):

    def decorate(func):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logname = name if name else func.__module__

        log = logging.getLogger(logname)
        log.setLevel(logging.INFO)      # 设置log级别

        fh = logging.FileHandler('test.log')    # 写入文件中
        fh.setFormatter(formatter)      # 文件中定义输出格式
        log.addHandler(fh)              # 给logger添加handler

        ch = logging.StreamHandler()    # 在控制台输出
        ch.setFormatter(formatter)      # 定义handler的输出格式
        log.addHandler(ch)              # 给logger添加handler

        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            time1 = datetime.datetime.now()
            res = func(*args, **kwargs)
            time2 = datetime.datetime.now()
            log.log(level, 'Function: {} , runtime: {}'.format(logmsg, time2 - time1))
            return res

        return wrapper
    return decorate

@logged(logging.INFO)
def add(x, y):
    time.sleep(5)
    return x + y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print (add(3, 6))
spam()



