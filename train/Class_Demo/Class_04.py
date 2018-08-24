#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/7

Describe: 类的特殊方法
#__doc__:类的描述信息
print Foo.__doc__       #类的特殊方法介绍
#__module__:表示当前操作的对象在哪个模块
print p1.__module__     #Class_01
#__class__:表示当前操作的对象的类是哪个类
print p1.__class__      #<class 'Class_01.Person'>
#__init__:构造方法,通过类创建对象时,自动触发执行
#__del__:析构方法,当对象在内存中被释放时,自动触发执行
#__call__:对象后面加括号触发执行,即对象() 或者类()()执行call定义的方法
#__dict__:类或对象的所有成员
p1 = Person('1','2')
print 'person-----',Person.__dict__
print 'dict-----',p1.__dict__
#__str__:类中定义了__str__方法,在打印对象时,默认输出该方法的return值
#__getitem__,__setitem__,__delitem__:用于索引操作,如字典
#__getslice__,__setslice__,__delslice__:用于分片操作,如列表
#__iter__:用于迭代器,列表、字典、元祖可以for循环,是因为类型内部定义了__iter__
#__new__和__metaclass__

'''


class Foo(object):
    """
    类的特殊方法介绍
    """

    def __new__(cls, *args, **kwargs):
        print '__new__'
        return cls

    def __init__(self):
        self.name = 'ttxsgoto'

    def __del__(self):
        print 'del'
        return

    def __call__(self, *args, **kwargs):
        return '__call__'

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        print '__getitem__', item
        return

    def __setitem__(self, key, value):
        print '__setitem__', key, value
        return

    def __delitem__(self, key):
        print '__delitem__', key
        return

    def __iter__(self):
        return iter(self.name)


# __doc__:类的描述信息
print Foo.__doc__  # 类的特殊方法介绍

f = Foo()
print f.__module__  # __main__
print f.__class__  # <class '__main__.Foo'>
print f()  # __call__
print Foo.__dict__
print f.__dict__  # {'name': 'ttxsgoto'}
print f  # ttxsgoto
f1 = f['key1']  # __getitem__ key1
f['key2'] = 'value2'  # __setitem__ key2 value2
del f['key2']  # __delitem__ key2

item = Foo()
for i in item:
    print i

# from Class_01 import Person
#
# p1 = Person('1','2')
# print 'person-----',Person.__dict__
# print 'dict-----',p1.__dict__

# __module__:表示当前操作的对象在哪个模块
# print p1.__module__     #Class_01


# __class__:表示当前操作的对象的类是哪个类
# print p1.__class__      #<class 'Class_01.Person'>

# __init__:构造方法,通过类创建对象时,自动触发执行
# __del__:析构方法,当对象在内存中被释放时,自动触发执行
