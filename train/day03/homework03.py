#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年5月5日

@author: zhongqiang

Describe: 作业
'''
from __future__ import unicode_literals,print_function
from mongoengine import  Document,StringField,DateTimeField
from mongoengine import  connect
import datetime
 
from flask import Flask
import flask_admin as admin
from flask_admin.contrib.mongoengine import ModelView
from atexit import register
from bsddb.test.test_all import verbose

"""
class Host(Document):
    
    name = StringField()
    add_time = DateTimeField(default=datetime.datetime.now())
    
    meta = {
            'collection':'host',
#             'collection':'idc',
        }
    
data = Host(name="ttxs2")
data.save()

if __name__ =='__main__':
    from flask import Flask
    import flask_admin as admin
    from flask_admin.contrib.mongoengine import ModelView
    
    app = Flask('hello')
    app.config['SECRET_KEY']='1234567890'
    
    admin = admin.Admin(app,u'资产管理系统')
    admin.add_view(ModelView(Host))         #添加视图
    app.run('0.0.0.0', 8080, debug=True)
"""


class User(Document):
    name = StringField(verbose_name="用户名")
    email = StringField(verbose_name="邮箱")
    password = StringField(verbose_name="密码")
    register_time = DateTimeField(default=datetime.datetime.now(),auto_now=True,verbose_name="注册时间")
    
    meta = {
            'collection':'User',
    }
    
    
#     def __init__(self,username,email,password,register_time):
#         self.username = username
#         self.email = email
#         self.password = password
#         self.register_time = register_time
#     
#     def __unicode__(self):
#         pass
#     
#     meta = {
#             'collection':'User',
#     }
#     def get_active_days(self):
#         pass
#     

class Hostinfo(Document):
    """
    主机信息
    """
    
    
    name = StringField(verbose_name="名称")
    ip = StringField()
    internal_ip = StringField()
    cpu = StringField()
    disk = StringField()
    
    meta = {
            'collection':'hostinfo',
    }
    
#     def __init__(self,name,ip,cpu,internal_ip,disk):
#         self.name = name
#         self.ip = ip
#         self.internal_ip = internal_ip
#         self.cpu = cpu
#         self.disk = disk
#         
#     meta = {
#             'collection':'hostinfo',
#     }
#     
#     def brief_info(self):
#         return self.name,self.ip,self.cpu,self.disk

















