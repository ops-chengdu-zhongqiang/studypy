#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/5

Describe:定时任务
启动worker进程;每次修改task代码后,需要restart  celery 进程;
cd /Users/study/studypy/train/celery_demo && celery -A celery_app_cron.init worker --loglevel=INFO
cd /Users/study/studypy/train/celery_demo && celery -A celery_app_cron.init beat

放在一起执行:
cd /Users/study/studypy/train/celery_demo && celery -B -A celery_app_cron.init worker --loglevel=INFO
'''
from celery import Celery

ttxsgoto = Celery("cron")

ttxsgoto.config_from_object('celery_app_cron.celeryconfig')
