#!/usr/bin/env python
#coding:utf-8

import atexit
import os

def not_called():
	print "This should not be called."
atexit.register(not_called)
print "Registering"


print "Registered"

print "Exiting..."
#os._exit(0)



#使用装饰器添加
print "Registering"
@atexit.register
def not_calling():
	print "This should be called......."

print "Registered"
#os._exit(0)
