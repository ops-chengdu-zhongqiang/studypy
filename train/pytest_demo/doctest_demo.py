#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/4/21

Describe:
doctest 是一个 Python 发行版自带的标准模块。
doctest 的两种方式:
    - 嵌入到源代码
    - 独立文件
    - doctest 模块会搜索那些看起来像交互式会话的 Python 代码片段，然后尝试执行并验证结果
'''
import doctest

def mult(a, b):
    """
    >>> mult(2,3)
    6
    >>> mult('ab',3)
    'ababab'
    """
    return a*b


def other_mult(a,b):
    return a*b


if __name__ == '__main__':
    # import doctest
    #doctest.testmod(verbose=True) #verbose 参数用于控制是否输出详细信息,默认为False
    doctest.testmod(verbose=True)
    doctest.testfile('doctest.txt')









