#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/3/3

Describe: 多个参数*args,**kwargs

'''

def auth_arg(func):
    def inner(*args, **kwargs):
        print "before"
        func(*args, **kwargs)
        print "after"
    return inner

@auth_arg
def f2(*args, **kwargs):
    print "This is f1 function-----",args,kwargs

f2('abc',1,'xxx',**{'a':1})

f2(**{'a':1})


