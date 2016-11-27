#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月7日

@author: zhongqiang

Describe: 
'''
from __future__ import print_function
from __future__ import unicode_literals
import doctest



def hello_add(x,y):
    """
    测试加法实例
    >>> 1 + 2
    3
    >>> hello_add(4,5)
    9
    >>> hello_add(4,5)
    5
    """
    z = x+y

    return z
def hello_substract(x,y):
    return x - y

if __name__ == '__main__':
    doctest.testmod()
    z = hello_add(10, 10)
    assert z == 20




