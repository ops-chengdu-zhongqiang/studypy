#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/3/3

Describe: 有返回值

'''

def auth_arg(func):
    def inner(*args, **kwargs):
        print "before"
        ret1,ret2 = func(*args, **kwargs) #通过ret来接收func函数的返回值
        print "after"
        return ret1, ret2  #返回func函数的返回值
    return inner

@auth_arg
def f3(*args, **kwargs):
    return  args,kwargs

ret1, ret2 = f3('abc',1,'xxx',**{'a':1})
print '============'
print ret1, ret2


# def auth_arg(list1=[]):
#     if not list1:
#         print 'None ....'
#         return []
#     new_list = []
#     for li in list1:
#         li += 'a'
#         new_list.append(li)
#     print new_list
#     def inner(func):
#         print 'Before'
#         def in_inner(*args, **kwargs):
#             ret1, ret2 = func(*args, **kwargs)
#             return ret1, ret2
#         return in_inner
#     return inner
#
# @auth_arg(list1=['a', '1'])
# def f3(*args, **kwargs):
#     print "f3 ---", args, kwargs
#     return args, kwargs
#
# a = [1,2]
# dict1={}
# dict1['ttxs'] = 'goto'
#
# f3(a, **dict1)

