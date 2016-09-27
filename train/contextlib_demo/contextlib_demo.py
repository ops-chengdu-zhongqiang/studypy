#!/usr/bin/env python
#coding:utf-8

class WithinContext(object):
	def __init__(self,context):
		print "WithinContext.__init__(%s) " %context

	def do_something(self):
		print "WithinContext.do_something()"

	def __del__(self):
		print "WithinContext.__del__"

class Context(object):
	def __init__(self):
		print "Context.__init__()"

	def __enter__(self):
		"""
		在主体代码执行前执行
		"""
		print "Context.__enter__()"
		return WithinContext(self)

	def __exit__(self,exc_type,exc_val,exc_tb):
		"""
		在主体代码执行后执行
		"""
		print "Context.__exit__()"

with Context() as c :
	"""
	as后面的变量是在__enter__函数中返回的
	"""
	c.do_something()

#执行结果：
Context.__init__()
Context.__enter__()
WithinContext.__init__(<__main__.Context object at 0x7f95045167d0>) 
WithinContext.do_something()
Context.__exit__()
WithinContext.__del__
