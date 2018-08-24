#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/25

Describe:
    - 给字符串加html标签
'''


def abc(*args, **kwargs):
    print 'kwargs----', kwargs, args
    x = kwargs.get('a')

    def tag0(func):
        def wapper(xxx):
            c = func(xxx)
            return '{}{}{}'.format(x, c, x)

        return wapper

    return tag0


def tag(tag1):
    print tag1

    def wapper(func):
        def xxx(args):
            c = func(args)
            return '{}{}{}'.format(tag1, c, tag1)

        return xxx

    return wapper


# @tag(tag1='<p><dev>')
@abc([1, 2, 3], a='abc')
def upper1(text):
    text1 = text.upper()
    return text1


print upper1('abc')
