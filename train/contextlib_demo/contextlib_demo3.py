#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/3/16

Describe:执行function前后执行相关代码
'''
from contextlib import contextmanager

@contextmanager
def tag(name):
    print 'before---',name
    yield
    print 'after----',name

def abc():
    print 'hello world'

with tag('ttxsgoto'):
    abc()


