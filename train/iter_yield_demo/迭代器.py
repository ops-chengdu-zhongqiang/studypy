#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/15

Describe:
迭代器对象，需要同时满足下列两个方法：
next():返回迭代器的下一个元素
__iter__:返回迭代器对象本身

定义一个迭代器：
names = iter(["a","b","d"])
使用：
print (names.next())
当容器中没有可访问的元素后，next()方法将会抛出一个StopIteration异常终止迭代器

当我们使用for语句的时候，for语句就会自动的通过__iter__()方法来获得迭代器对象，并且通过next()方法来获取下一个元素
'''

list1 = [1,2,3]
tuple1 = (1,2,3)
dict1 = {'a':1,'b':2}

list1_iter = iter(list1)
tuple1_iter = iter(tuple1)
dict1_iter = iter(dict1)
print list1_iter, tuple1_iter, dict1_iter

print dict1_iter.next()
print dict1_iter.next()
print dict1_iter.next()


