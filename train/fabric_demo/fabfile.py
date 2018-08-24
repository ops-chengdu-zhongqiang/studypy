#!/usr/bin/env python
#coding: utf_8

from __future__ import with_statement
from __future__ import unicode_literals

import time
from fabric.api import local, cd, run, settings,env,task
from fabric.context_managers import prefix
from fabric.contrib.console import confirm
from fabric.decorators import roles, parallel, serial, runs_once
from fabric.colors import *
from fabric.operations import prompt

env.hosts=['192.168.0.192','192.168.0.200']
env.password='POIlkj,mn'
env.user='root'
#env.roledefs={'web1':['192.168.0.192'],'web2':['192.168.0.200']}

__all__ = ['local_deploy','run1','hello','test_confirm','test_prompt']     #定义全局可用的tasks列表

@task
def hello(name):
    '''
    传递参数: fab hello:name=ttxsgoto
    '''
    print "hello------------{}".format(name)

@task
def local_deploy():
    '''
    执行本地命令
    :return:
    '''
    with settings(warn_only=True):
        return local('ls /Users/study/studypy/train/fabric_demo/fabfile.py')
    # local('cat fabfile.py')

@task   #标识为fab可调用
@roles('web2')  #调用roles
def with_deploy():
    '''
    执行with函数
    :return:
    lcd 本地执行,cd 远程执行
    '''
    dir = '/etc/network/'
    with cd(dir):
        run('ls .')

@task
def dir():
    """
    remote list
    :return:
    """
    dir = '/etc/'
    with cd(dir):
        run('ls -l rc.local')

@task(default=True)
@parallel(pool_size=3)
def run1():
    """
    启动
    :return:
    """
    print time.ctime()
    hello('ttxsgoto')
    local_deploy()
    dir()
    time.sleep(2)
    print time.ctime()
    print(yellow("This text is green!",bold=True)) #用于打印显示颜色, bold：用于设置粗体

@task()
def runserver():
    with prefix('workon ownserver'):
        run('cd /date/ownserver && python manage.py runserver 0.0.0.0:8000')

@task()
def test_confirm():
    '''
    测试交互确认
    :return:
    '''
    INFO = confirm('Are you sure?[yes/no]?')
    if INFO:
        print 'yes'
    else:
        print 'no'

@task()
def test_prompt():
    '''
    测试输入信息
    :return:
    '''
    Text = prompt('Input word:')
    print '-----',Text
