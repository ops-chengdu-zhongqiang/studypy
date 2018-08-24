#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/5/2

Describe:
    - 类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
'''


class Foo(object):
    def __init__(self, func):
        print "__init__  function"
        self.func = func

    def __call__(self, *args, **kwargs):
        print "Before..."
        self.func()
        print "After..."


@Foo
def bar():
    print 'bar funtion()'


bar()

print '#######################################'


class Decorate(object):
    def __init__(self, list1):
        self.list1 = list1

    def __call__(self, func):
        if not self.list1:
            print 'None ....'
            raise Exception('LIST is  Null ')
        new_list = []
        for li in self.list1:
            li += 'a'
            new_list.append(li)
        print new_list

        def inner(*args, **kwargs):
            ret1, ret2 = func(*args, **kwargs)
            return ret1, ret2

        return inner


@Decorate(list1=[])
def f3(*args, **kwargs):
    print "f3  function", args, kwargs
    return args, kwargs

# a = [1,2]
# dict1={}
# dict1['ttxs'] = 'goto'
# c = f3(a, **dict1)
# print c
