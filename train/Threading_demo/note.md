**多线程**
---
在python虚拟机中的访问由**全局解释器锁（GIL）**控制，由于有了这把锁能保证同一时刻只有一个线程在运行，在多线程环境下，python虚拟机按照如下方式运行：
1. 设置GIL
1. 切换到一个线程中运行
1. 运行：
1.  a指定数量的字节码的指令，或者
1.   b线程主动让出控制（可以调用time.sleep(0)）
1. 把线程设置为睡眠状态
1. 解锁GIL
1. 在重复以上所有步骤

#### threading.Thread模块
---
threading.Thread 作用：创建线程实例
- start()    开始一个线程的执行
- run()    定义线程的功能的函数（一般会被之类重写）
- join(timeout=None)  程序挂起，直到子线程结束，在执行主线程，如果给了timeout，则最多阻塞timeout秒
- getName()    返回线程的名字
- setName()    设置线程的名字
- isAlive()    检查线程是否成活
- isDaemon()   是否等待线程执行完成后在执行主进程，默认为false
- setDeaemon() 设置为daemoe模式，setDeaemon(True)，不等子线程执行完成，直接执行主线程；如果在主线程没有结束时，子线程会执行直到主线程结束，子线程也结束



