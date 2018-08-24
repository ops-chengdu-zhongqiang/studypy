#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/5

Describe: 
'''

import time
from .init import ttxsgoto

@ttxsgoto.task
def add(x, y):
    time.sleep(5)
    return x + y

