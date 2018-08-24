#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/4/18

Describe: 
'''


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''
    返回一个类对象,将属性都转为大写形式
    '''
    # 选择所有不以'__'开头的属性
    print '----', future_class_attr.items()
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    print 'xxxx', attrs
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


class Foo(object):
    # 作用到这个模块的所有类
    __metaclass__ = upper_attr
    bar = 'ttxsgoto'


print '------------'
print hasattr(Foo, 'bar')
print hasattr(Foo, 'BAR')
print Foo.BAR


#########class type#########
class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情

    # 方法一
    # def __new__(cls, future_class_name, future_class_parents, future_class_attr):
    #     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    #     uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    #     return type.__new__(cls, future_class_name, future_class_parents, uppercase_attr)

    # 方法二
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaClass, cls).__new__(cls, name, bases, uppercase_attr)


class Foo(object):
    # 作用到这个模块的所有类
    __metaclass__ = UpperAttrMetaClass
    bar = 'ttxsgoto'


print '==========='
print hasattr(Foo, 'bar')
print hasattr(Foo, 'BAR')
print Foo.BAR
print getattr(Foo, 'BAR', 'A')
