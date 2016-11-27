#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年5月4日

@author: zhongqiang

Describe: 
'''

from __future__ import print_function,unicode_literals
import datetime

class User(object):
    
#     regiter_time = datetime.datetime(2014,12,10)
#     username = "xxts"
    def __init__(self,username="ttxs"):
        self.username = username
        
    def __str__(self):
        return "User: %s " %self.username
    
    def get_register_date(self):
        return datetime.datetime.now() - self.regiter_time
    
    def get_register_days(self):
        delta = self.get_register_date()
        return delta.days
    
    @staticmethod
    def print_hello(x="hello"):
        print (x)
    
    @property
    def register_days(self):
        return  self.get_register_days()
    
    def register_seconds(self):
        delta = self.get_register_date()
        return delta.seconds

class Utils(object):
    @staticmethod
    def print_json(data):
        import json
        print (json.dumps(data,indent=4,ensure_ascii=False))


class SubUser(User):
    def __init__(self,username=""):
        self.username = "sub_username: %s " %username
    def get_register_days(self): #类继承User，并重写get_register_days方法
        days = User.get_register_days(self)
        return str(days)

if __name__ == '__main__':
    user = User()
    user.username ="ttxs"
    print (user.username)
    
    days1 = user.get_register_days()
    print (days1,type(days1))
    user2 = SubUser()
    days2 = user2.get_register_days()
    print (days2,type(days2))
     
    user3 = User(username="ttxs01")
     
    print (user3) #执行的是str方法
     
    user4 = SubUser(username="ttxs02")
     
    print (user4)
     
    User.print_hello(x="hello-world")
     
    Utils.print_json(data={'name':"天天向上",'id':100,'other':{1:2}})
     
    print (user4.register_days)







