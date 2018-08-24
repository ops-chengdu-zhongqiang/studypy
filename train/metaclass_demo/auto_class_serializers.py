#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/6/9

Describe:
    - 通过元类,自动添加动态类,动态字段添加
'''

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest_framework_api.settings')
application = get_wsgi_application()

from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer


class Comment(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


words = {
    "email": "zhongqiang@163.com",
    "content": "test",
    "datetime": datetime.now(),
    "aaa": "1",
    "bbb": "2",
    "ccc": "3",
}

works_value = {
    "email": "email",
    "content": "string",
    "datetime": "datetime",
    "aaa": "string",
    "bbb": "string",
    "ccc": "string",
}

comment = Comment(**words)


# print comment.email, comment.content, comment.datetime, comment.a, comment.b, comment.c

class CommentSerializer(serializers.Serializer):
    """
    DRF 原始方法
    """

    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    datetime = serializers.DateTimeField()
    a = serializers.IntegerField()
    b = serializers.CharField(max_length=100)
    c = serializers.CharField(max_length=100)


# serializer = CommentSerializer(comment)

TYPE_DICT = {
    'bool': serializers.BooleanField(default=True),
    'string': serializers.CharField(max_length=100),
    'datetime': serializers.DateTimeField(),
    'int': serializers.IntegerField(),
    'email': serializers.EmailField()
}


############# 函数实现方式 begin ###############
def get_type(type):
    return TYPE_DICT.get(type)


def set_serializer(**kwargs):
    return {k: get_type(v) for k, v in kwargs.items()}


def get_modelserializer(model):
    return str(model) + "Serializer"


def get_serializer(modelserializer, **kwargs):
    return type(modelserializer, (serializers.Serializer,), kwargs)


# dd = set_serializer(**works_value)
# ee = get_serializer(modelserializer=get_modelserializer('Comment'), **dd)
# serializer = ee(comment)
############# 函数实现方式 end ###############

###### 类实现自动添加serializer方式begin ######

class AutoSerializer(object):
    """
    自动生成serializer
    """

    def __init__(self, model, fields):
        self.model = model
        self.fields = fields

    def get_field(self):
        return {k: TYPE_DICT.get(v) for k, v in self.fields.items()}

    def get_model(self):
        return str(self.model) + "Serializer"

    def get_serializer(self):
        """
        动态生成类
        """
        # from rest_framework import serializers
        print '---------get_model-----', self.get_model()
        print '---------get_field-----', self.get_field()
        return type(self.get_model(), (serializers.Serializer,), self.get_field())


commentserializer = AutoSerializer(model=Comment.__name__, fields=works_value)
print 'commentserializer-----', commentserializer
serializer = commentserializer.get_serializer()(comment)

print 'serializer-------', serializer
data = serializer.data
print data

# print type(serializer.data)

# jsons = JSONRenderer().render(serializer.data)
# print JSONRenderer().render(serializer.data)
# print type(jsons)
