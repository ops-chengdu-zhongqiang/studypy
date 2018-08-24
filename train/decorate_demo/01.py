#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/3/3

Describe: 最简单的装饰器
'''

from functools import wraps


def auth(func):
    # @wraps(func)
    def inner():
        print "before"
        func()
        print "after"

    return inner


@auth  # @auth ==> f1 = auth(f1) ==>f1() 相当于执行inner函数，func为f1函数
def f1():
    print "This is f1 function"


f1()

print f1, f1.__name__


# def auth_arg(func):
#     def inner(*args, **kwargs):  # 传递一个/多个参数
#         print "before"
#         re1 , re2 = func(*args, **kwargs)  # 相当于f2(*args, **kwargs)函数
#
#         print "after"
#
#         return re1, re2
#     return inner
#
#
# @auth_arg
# def f2(*args, **kwargs):
#     print  args,kwargs
#     return args, kwargs
#
# key1 = 'ttxsgoto'
# dict1 = {}
# dict1['ttxs'] = 'goto'
# print f2(key1, **dict1)


def w1(func):
    def inner():
        print "before01"
        func()
        print "after01"

    return inner


def w2(func):
    def inner():
        print "before02"
        func()
        print "after02"

    return inner


@w2
@w1
def foo():
    print "foo"


foo()
