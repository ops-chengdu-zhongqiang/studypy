#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/5

Describe:异步执行
启动worker进程;每次修改task代码后,需要restart  celery 进程;
cd /Users/study/studypy/train/celery_demo && celery worker -A celery_app.init --loglevel=INFO

'''
from celery import Celery

ttxsgoto = Celery("ttxsgoto")   #创建一个celery任务

ttxsgoto.config_from_object('celery_app.celeryconfig')  #将配置导入到celery对象中


