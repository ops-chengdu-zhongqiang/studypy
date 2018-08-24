#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/1/5

Describe: 
'''
from datetime import timedelta
from celery.schedules import crontab
from celery import Celery

BROKER_URL = 'redis://127.0.0.1:6379'  # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend
CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC

CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_app_cron.task1',
    'celery_app_cron.task2'
)

# ttxsgoto = Celery("cron",broker= BROKER_URL, backend= CELERY_RESULT_BACKEND)

# 定时任务设置
CELERYBEAT_SCHEDULE = {
    'add-every-30s': {
        'task': 'celery_app_cron.task1.add',  # 任务执行的函数
        'schedule': timedelta(seconds=30),  # 每30s执行一次
        'args': (5, 8)  # 任务函数参数
    },

    'multiply-erver-10s': {
        'task': 'celery_app_cron.task2.multiply',
        # 'schedule':crontab(hour=9,minute=30),      #cron计划任务,每天9:30进行
        'schedule': timedelta(seconds=10),
        'args': (3, 7)  # 任务参数
    }
}
