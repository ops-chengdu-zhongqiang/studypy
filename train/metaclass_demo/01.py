#!/usr/bin/env python
# coding: utf_8
'''
__author__ = ‘zhongqiang‘

Created on  17/4/13

Describe:
http://blog.jobbole.com/21351/
'''


################类也是对象####################
# 只要使用关键字class，Python解释器在执行的时候就会创建一个对象
# 类的本质也是对象,可进行如下操作:
# - 赋值给一个变量
# - copy
# - 添加属性
# - 将它作为函数参数进行传递

class ObjectCreator(object):
    pass


my_obj = ObjectCreator()
print my_obj

print hasattr(ObjectCreator, 'xxx')
ObjectCreator.xxx = 'xxx'
print hasattr(ObjectCreator, 'xxx')
print ObjectCreator.__dict__

Obj_log = ObjectCreator

print Obj_log, Obj_log()
print type(ObjectCreator), type(ObjectCreator())
# <type 'type'> <class '__main__.ObjectCreator'>

################类动态创建####################







# type有一种完全不同的能力，它也能动态的创建类。type可以接受一个类的描述作为参数，然后返回一个类
# type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
# type 接受一个字典来为类定义属性


Type_Class = type('Type_Class', (), {})  # 返回一个类对象

print Type_Class


class Foo(object):
    bar = True


# 两者等价
Foo = type('Foo', (), {'bar': True})

print Foo.bar, Foo().bar

################元 类####################
'''
元类就是用来创建这些类（对象）的，元类就是类的类,即:
MyClass = MetaClass()
MyObject = MyClass()

MyClass = type('MyClass', (), {})
type实际上是一个元类,type就是Python在背后用来创建所有类的元类,用来创建类对象的类

__class__ : 查看对象所属类
'''
print Foo.__class__
a = 12
print a.__class__, a.__class__.__class__


def Fun():
    pass


print Fun.__class__
print Fun.__class__.__class__.__class__

##########__metaclass__属性#############
# class Foo(object):
#     __metaclass__ = 'abc'
#     pass

'''
元类的主要目的就是为了当创建类时能够自动地改变类,元类是类的类
'''


class Bar(object):
    pass


'''
以上代码说明:
Python会在类的定义中寻找__metaclass__属性，如果找到了，Python就会用它来创建类Foo，
如果没有找到，就会用内建的type来创建这个类
'''


class Foo(Bar):
    pass


'''
以上代码说明:
Foo中有__metaclass__这个属性吗？如果有，Python会在内存中通过__metaclass__创建一个
名字为Foo的类对象;如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找
__metaclass__属性，并尝试做和前面同样的操作(如上)
如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，
并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

即首先在当前类里找__metaclass__,如果没有,向父类中找,如果没有,在向模块层面中找,如果都没有
找到。使用python内置的type来创建这个类对象

__metaclass__:中放置可以创建一个类的东西(type),或者任何使用到type或者子类化type的东东都可以

'''

##################自定义元类#############
'''
元类的主要目的就是为了当创建类时能够自动地改变类。通常你会为API做这样的事情，
你希望可以创建符合当前上下文的类
'''


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''
    返回一个类对象,将属性都转为大写形式
    '''
    # 选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)


class Foo(object):
    # 作用到这个模块的所有类
    __metaclass__ = upper_attr
    bar = 'ttxsgoto'


print '------------'
print hasattr(Foo, 'bar')
