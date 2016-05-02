#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月1日

@author: zhongqiang

Describe: 类的继承,多继承
'''

"""
class Father(object):
    def __init__(self):
        self.Fname ="father"
    
    def Func(self):
        print "Father func "
    
    def run(self):
        print "Father func_public"


class Son(Father):
    def __init__(self):
        self.Sname = "son"
        
    def Bar(self):
        print "Son bar_function"
        
    def run1(self):
        print "Son func_public"
    
    def run(self): #重写父类的方法
        Father.run(self)
        print "xxxxxxxxxx"

s1 = Son()
s1.Func()
s1.run()
"""

class A(object):
    def __init__(self):
        print "A class"
    def run(self):
        print "THis is A run Function"

class B(A):
    def __init__(self):
        print "B class"
        A.__init__(self)    #新式类继承init函数，方法一
#         super(B, self).__init__() #新式类继承init函数，方法二
#     def run(self):
#         print "This is B run Function"

class C(A):
    def __init__(self):
        print "C class"
    def run(self):
        print "This is C run Function"

class D(B,C):
    def __init__(self):
        print "D class"

d = D()
d.run()
"""
经典类：D-B-A-C
结果：
D class
THis is A run Function

新式类：
结果： D-B-C-A
D class
This is C run Function
"""

























