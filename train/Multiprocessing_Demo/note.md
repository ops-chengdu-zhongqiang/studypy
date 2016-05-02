### **多进程**
---
###Process
---
**方法（类似于threading）：**
- is_alive()
- join(timeout)
- run()
- start() #开始某个进程

**属性：**
- daemon（要通过start()设置，并在之前设置）
- exitcode(进程在运行时为None、如果为–N，表示被信号N结束）
- name #线程的名称
- pid	#线程的pid

**多进程运行方式**
1.函数调用
```python
#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Process
import time

def run(info_list,n):
    info_list.append(n)
    print info_list

info=[]
for i in range(10):
    p = Process(target=run,args=(info,i))
    p.start()
print p.pid
print p.name
print p.is_alive()

```

2.通过类继承运行
```python
#!/usr/bin/env python
#coding:utf-8

import multiprocessing
import time

class MyProcess(multiprocessing.Process): #继承Process
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        print "Begin----"
        myfunction(self.interval)
        print "End-----"

def myfunction(ms):
    n = 5
    while n > 0:
        print("the time is %s" %format(time.ctime()))
        time.sleep(ms)
        n -= 1

if __init__== '__main__':
    p = MyProcess(1)
    p.daemon = True  #当子进程设置了daemon属性时,默认为false，主进程结束，子进程也随之结束
    p.start()  #进程p调用start()方法时，自动调用run()方法
    time.sleep(3)
    print "Main Process is Over...."

```

###Pool
---
Pool可以提供指定数量的进程，给用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。

**方法：**
- apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的
- close() 关闭pool，使其不再接受新的任务
- terminate() 结束工作进程，不在处理未完成的任务
- join()  主进程阻塞(挂起),等待子进程的退出，join方法要在close或者terminate之后才能使用

```python
#!/usr/bin/env python
#coding:utf-8

from multiprocessing import Pool
import time

def f(x):
    print x*x
    time.sleep(1)
    return x*x

pool = Pool(processes=5) #最多5个进程
res_list = []

print "------------"
print "执行方法一"
#执行方法一
print pool.map(f,range(10))  #将函数放在5个进程中执行
print "end 01 -------"

#执行方法二
print "执行方法二"
for i in range(10):
    res = pool.apply_async(f,(i,)) #apply_async 设置为异步
    #res.get() #取线程执行的结果
    res_list.append(res)  #将执行结果放入列表中

for r in res_list: #循环列表得到结果
    print r.get()

print "Over over ..."
```