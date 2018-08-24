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
###### 常用字段 ######
- name 项目名称
- version 项目当前的版本，1.0.0表示1.0.0版，目前还处于开发阶段
- description 包的简单描述
- long_description=long_description, 较长的描述
- url 为项目访问地址
- author 为项目开发人员
- author_email 为项目开发人员邮件
- license 为本项目遵循的授权许可
- classifiers 有很多设置，具体内容可以参考官方文档, https://pypi.python.org/pypi?%3Aaction=list_classifiers
- keywords 是本项目的关键词，理解为标签
- packages 指定包,如果很多可以使用find_packages & exclude
- install_requires 依赖包安装
- extras_require 额外的依赖包

##### 参考链接
- https://packaging.python.org/tutorials/distributing-packages/#name
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://github.com/celery/celery/blob/master/setup.py

==============
当前目录结构:

├── README
├── package_demo
│   ├── __init__.py
│   └── now_time.py
└── setup.py


-------------
python setup.py sdist

├── Package_demo.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── requires.txt
│   └── top_level.txt
├── README
├── dist
│   └── Package_demo-1.0.0.tar.gz
├── package_demo
│   ├── __init__.py
│   └── now_time.py
└── setup.py
'''


from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README')) as f:
    long_description = f.read()



install_requires=[
    'gitchangelog',
]

setup(

    name='Package_demo',
    version='1.0.0',
    description='setup package demo',
    long_description=long_description,
    url='https://github.com/',
    author='ttxsgoto',
    author_email='359450323@qq.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='Package_demo',
    # packages=find_packages(
    #     where='.',
    #     exclude=['contrib', 'docs', 'tests'], # 排除某些包
    # ),
    packages=['package_demo'],
    install_requires=install_requires,
)
