#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年5月4日

@author: zhongqiang

Describe: 
'''

from __future__ import unicode_literals,print_function
from mongoengine import  Document,StringField,DateTimeField
from mongoengine import  connect
import datetime
from homework03 import *

HOST = '192.168.6.228'

connect('ttxs', host=HOST)

class Host(Document):
    
    name = StringField()
    add_time = DateTimeField(default=datetime.datetime.now())
    
    meta = {
            'collection':'host',
        }
    
# data = Host(name="ttxs2")
# data.save()

# user = User(name="user01",email="user01@163.com",password="123")
# user.save()

# hostinfo = Hostinfo(name="hostinfo01",ip="1.1.1.1",internal_ip="2.2.2.2",cpu="8",disk="200GB")
# hostinfo.save()

if __name__ =='__main__':
    from flask import Flask
    import flask_admin as admin
    from flask_admin.contrib.mongoengine import ModelView
    
    app = Flask('hello')
    app.config['SECRET_KEY']='1234567890'
    
    admin = admin.Admin(app,u'资产管理系统')
    admin.add_view(ModelView(Host))         #添加视图
    admin.add_view(ModelView(User))
    admin.add_view(ModelView(Hostinfo))
    app.run('0.0.0.0', 8080, debug=True) 






























