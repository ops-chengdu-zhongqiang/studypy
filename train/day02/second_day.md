
#py_day02 
###DRY:Do not repeat yourself!!!
------
-  **tuple**
-  **List**
-  **Set**
-  **列表解析**
-  **迭代器**
-  **yield**
-  **生成器**
-  **浅拷贝和深拷贝**
-  **json**
-  **enumerate枚举**
-  **Collections**

------

##tuple  
内存使用不可变，数据不可变

------
##List
list.append():在列表末尾添加新的对象，添加的对象是什么类型，添加的也是什么类型
list.extend():用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表），最后得到的为一个单个序列
```python
mylist =[1,2,0,'abc']
a=('aa',22)
mylist.append(('aa',44))
print mylist    #[1, 2, 0, 'abc', ('aa', 44)]
mylist.extend(('ab','cd'))
print mylist    #[1, 2, 0, 'abc', ('aa', 44), 'ab', 'cd']

结果：
[1, 2, 0, 'abc', ('aa', 44)]
[1, 2, 0, 'abc', ('aa', 44), 'ab', 'cd']
```

##Set
set  ：集合，无序不重复元素集合 ，都是唯一的 ,得到唯一的值 list(set(a))
```python
x = set('span')
y = set(['h','a','m'])
print x,y
print x&y #交集
print x|y #并集
print x-y #差集
a =[11,22,33,44,11,22]
b = set(a)
print a,b
c=(i for i in b)
d=[i for i in b]
print d
print c.next()    #生成器
结果：
set(['a', 'p', 's', 'n']) set(['a', 'h', 'm'])
set(['a'])
set(['a', 'p', 's', 'h', 'm', 'n'])
set(['p', 's', 'n'])
[11, 22, 33, 44, 11, 22] set([33, 11, 44, 22])
[33, 11, 44, 22]
33
```
------
##列表解析
如果想通过操作和处理一个序列来创建一个新的列表时可以使用列表解析和生成表达式
在需要改变列表而不是需要新建某个列表时，可以使用列表解析
```python
dirs=[i for i in lsdir if isdir(join(path,i))]
a = ['day-%d'%i for i in range(1,7)]
print a
b=[i for i in range(50) if i%3==0 or i % 5==0]
print b
print sum(b)
结果：
['day-1', 'day-2', 'day-3', 'day-4', 'day-5', 'day-6']
[0, 3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48]
543
```

##迭代器
迭代器 iter :存在内存中或者文件中，一次只能读取1个元素
是访问元素的一种方式，迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完后结束
迭代器的优点：不需要事项准备好整个迭代过程中的所有元素，迭代器仅在迭代到某个元素时才计算该元素，在这之前或之后，元素可以不存在或者被销毁，该特点使它特别适合用于遍历一个大的文件或集合，如几个G的文件
特点：
1.访问值不需要关心迭代器内部结构，仅需通过next()方法来不断取下一个内容
2.不能随机访问集合中的某个值，只能从头到尾依次访问
3.访问到一半时不能回退
4.用于循环大的数据集合，节约内存
方法：
next():返回迭代器的下一个元素
__iter__:返回迭代器对象本身

定义一个迭代器：
names = iter(["a","b","d"])
使用：
 print (names.next())
 
##yield
yield：每需要一个时，添加一个
简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5)【如下生成器代码】 不会执行 fab 函数，而是返回一个 iterable 对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。


##生成器（generator）
一个函数调用时返回一个迭代器，那么这个就叫生成器（generator），如果函数中包含yield语法，那么这个函数就变成了生成器
return作用：在一个生成器中，如果没有return，则默认执行到函数完毕；如果遇到return，如果在执行过程中return则会抛出StopIteration终止迭代 ,即return和yield 不能在同一个函数中同时出现
```python
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fab(5):
    print n
```

##浅拷贝和深拷贝
浅拷贝：共用一个内存区,利用切片操作和工厂方法list方法拷贝就叫浅拷贝，只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已
深拷贝:利用copy中的deepcopy方法进行拷贝就叫做深拷贝，外围和内部元素都进行了拷贝对象本身，而不是引用
[例子说明](http://www.01happy.com/python-shallow-copy-and-deep-copy/)
```python
import copy
copy.deepcopy()
```

##json
Python数据类型映射到JSON关系：

| Python | Json |
|--------|--------|
|    dict    |   object     |
|	list,tuple | array |
| str,unicode| string |
| int,long,float| number|
| True | true|
| False| false|
| None | null |


```python
from __future__ import unicode_literals   #解决字符串编码问题
import json
print json.dumps(d,indent=9)
print json.dumps(d_10,ensure_ascii=False)  中文字符显示，非乱码
with open('test.json','w') as f:
    json.dump(d,f)       写入json格式的数据
     json.dump(d,f,indent=2)     格式化读入，相应数据都占一行
dumps 写入json格式数据
得到原始数据，需要使用的json.loads()函数
```
##enumerate枚举
用于遍历序列中的元素以及它们的下标
```python
for i,file_x in enumerate(os.listdir('.')):
    if i >5:
        break
    elif i % 2 ==1:
        print file_x
yield file_x


for i ,file_x in enumerate(os.listdir('.'),start=1):  #start 从第一个开始打印
    print i,file_x

```

##Collections
Collections是Python内建的一个集合模块，提供了许多有用的集合类
-   nametuple：可以方便定义一种数据类型，它具备tuple的不变性，也可以根据属性来引用
-   Counter ：一个简单的计数器，用来统计
-   defaultdict：用于dict中Key不存在时，会抛出KeyError异常，可使用defaultdict返回一个默认值
-   OrderedDict：dict的key是无序的，在对dict做迭代是，可以通过orderedDict来保存key的顺序

```python
from collections import Counter, OrderedDict, defaultdict

cnt = Counter([1,1,2,3,4,5,56,67,76,78,78,89,89,78,78,90])
print cnt.most_common()  #统计所有值出现的次数
d = dict(cnt.most_common(10))
print d
print d.get(78)  #获取78出现的次数

dd = defaultdict(lambda : 'N/A')
dd['a']='1'
print dd['a']
print dd['xx']   #不存在的key，返回默认定义的值

d = dict([('a',1),('b',2),('c',3)])
print d
di = OrderedDict([('a',1),('b',2),('c',3)])  # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
print di
结果：
[(78, 4), (1, 2), (89, 2), (2, 1), (3, 1), (4, 1), (5, 1), (76, 1), (67, 1), (56, 1), (90, 1)]
{1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 76: 1, 78: 4, 67: 1, 56: 1, 89: 2}
4
1
N/A
{'a': 1, 'c': 3, 'b': 2}
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

