#!/usr/bin/env python
# coding:utf-8
'''
Created on 2016年5月1日

@author: zhongqiang

Describe: 抽象类接口
抽象类+抽象方法 = 接口
'''
"""
from abc import ABCMeta,abstractmethod
from bdb import foo

class Bar(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Func(self): #定义函数不做任何事情
        pass


class Foo(Bar):
    def __init__(self):
        print "__init__"
    
    def Func(self):
        print "sent something"

f = Foo()
f.Func()
"""


# 自定义异常，手动触发异常
class MyException(Exception):
    def __init__(self, msg):
        self.error = msg

    def __str__(self, *args, **kwargs):  #
        return self.error


obj = MyException('自定义错误信息')
print obj
raise MyException('自定义错误信息')
