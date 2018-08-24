#!/usr/bin/env python
#coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/14

Describe:
    - http://www.jianshu.com/p/f3a5392b8e25
    - https://packaging.python.org/tutorials/distributing-packages/
    - http://pythonhosted.org/distlib/overview.html#what-was-the-problem-with-packaging
    - https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi
    - https://github.com/celery/celery/blob/master/setup.py
    - https://packaging.python.org/key_projects/


==============
name为项目名称，和顶层目录名称一致;
version是项目当前的版本，1.0.0.dev1表示1.0.0版，目前还处于开发阶段
description是包的简单描述，这个包是做什么的
url为项目访问地址，我的项目放在github上。
author为项目开发人员名称
author_email为项目开发人员联系邮件
license为本项目遵循的授权许可
classifiers有很多设置，具体内容可以参考官方文档
keywords是本项目的关键词，理解为标签
packages是本项目包含哪些包,我这里只有一个名词为hive的包
==============
'''

from setuptools import setup, find_packages

install_requires=[
    'python-dateutil',
    'mongoengine==0.11.0',
    'pillow',
]

setup(
    name='xingyunhr_data',
    version='1.0.0.dev0',
    description='xingyunhr_data django models',
    url='https://github.com/ttxsgoto/studypy',
    author='ttxsgoto',
    author_email='zhongqiang2014@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='xingyunhr_data models',
    packages=find_packages(
        where='.',
        exclude=('test*',)
    ),
    # packages=['xingyunhr_data'],    # 是本项目包含哪些包
    install_requires=install_requires,  # 依赖包安装

)