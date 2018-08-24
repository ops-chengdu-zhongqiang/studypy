#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/5/7

Describe: 
'''


def no_new_attr(wrapped_setattr):
    def __setattr__(self, name, value):
        if hasattr(self, name):
            wrapped_setattr(self, name, value)
        else:
            raise AttributeError("Can't add attr {} in {}".format(name, self))

    return __setattr__


class NoNewAttrs(object):
    __setattr__ = no_new_attr(object.__setattr__)

    class __metaclass__(type):
        __setattr__ = no_new_attr(type.__setattr__)


class Person(NoNewAttrs):
    '''
    限制属性的设置
    '''
    firstname = None
    lastname = ''

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return 'Person(---{}---{})'.format(self.firstname, self.lastname)


me = Person('TTXS', 'GOTO')
print me


######################

class Chainmap(object):
    pass
