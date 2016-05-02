#!/usr/bin/env python
#coding:utf-8
'''
Created on 2016年5月1日

@author: zhongqiang

Describe: 
'''

class Person(object):
    name = "静态字段"
    
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    
    def run(self):
        print self.Name + "正在跑步"
    
    @staticmethod
    def run1():
        print "静态方法" 
     
    @property    #转换为特性，直接以属性的形式访问   
    def Bar(self):
        print self.Name
    
    def __del__(self):
        print "解释器要销毁了"

    def __call__(self):
        print "abc"
person1 = Person('人1',20)

person1()

#访问动态字段
print person1.Name
#访问动态方法
person1.run()

#访问静态字段
print Person.name
#访问静态方法
Person.run1()

#property的访问形式,直接以属性的形式访问
person1.Bar









