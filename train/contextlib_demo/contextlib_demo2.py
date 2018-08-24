#!/usr/bin/env python
#coding:utf-8
"""
contextlib中的contextmanager作为装饰器来提供一种针对函数级别的上下文管理机制.
"""
import contextlib

@contextlib.contextmanager
def make_context():
	print "entering"
	try:
		yield {}
	finally:
		print "exiting"

with make_context():
	print "inside with statement:", 'xxdsafds'

#执行结果：
'''
entering
inside with statement: {}
exiting
'''

print '11111111111111111'

# @contextlib.contextmanager
# def make_context(name):
# 	print "entering",name
# 	yield name
# 	print "exiting",name
#
# with contextlib.nested(make_context('A')) as (c):
# 	print "inside with statement: ",c
#
# #执行结果：
# '''
# entering A
# inside with statement:  ['A']
# exiting A
# '''
#
# with contextlib.nested(make_context('A'),make_context("B"),make_context("C")) as (A,B,C):
# 	"""
# 	nested用于创建嵌套的上下文
# 	"""
# 	print "inside with statement: ",A,B,C
#
# #执行结果：
# '''
# entering A
# entering B
# entering C
# inside with statement:  A B C
# exiting C
# exiting B
# exiting A
# '''
#
# class Door(object):
# 	def __init__(self):
# 		print "__init__()"
#
# 	def close(self):
# 		print "close()"
# 		return
#
# with contextlib.closing(Door()) as door:
# 	"""
# 	closing执行定义好的close函数
# 	"""
# 	print "inside with statement."
#
# #执行结果：
# '''
# __init__()
# inside with statement.
# close()
# '''
