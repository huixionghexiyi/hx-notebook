# 进程

# 在like Unix中，通过操作系统提供的fork()函数创建子进程，返回两次，一次返回到父进程，返回子进程的PID；一次返回到子进程，返回默认为0

# like unix 创建子进程
import os
print('process (%s) start ...',os.getpid()) # 
pid = os.fork() # linux 是fork()函数
if pid == 0:
    print('im child ,my pid (%s),parent pid (%s)',%(os.getpid(),os.getppid()))
else:
    print('my pid (%s),i created a child process (%s)',%(os.getpid(),pid)))

# 跨平台通用模块
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process (%s)'% os.getpid())
    p = Process(target=run_proc,args=('test',)) # 传入一个执行函数，和函数的参数，用start启动即可
    p.start() # 启动进程
    p.join() # 等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')

# 启动多个子进程，就用进程池的方式创建
from multiprocessing import Pool
import os,time,random
def long_time_taks(name):
    print('Run task %s(%s)'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

if __name__ == '__main__':
    print('Parent process %s'%os.getpid())
    p = Pool(4)
    for i in range(16):
        p.apply_async(long_time_taks,args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join() # join() 之前必须先close(),调用close()之后就不能添加新的Process
    print('All subprocesses done.')

# 需要注意，由于我们创建Pool对象的时候传入参数4，所以在task 4的时候需要等待0 1 2 3中有一个完成，才会执行，不是操作系统的限制。
# 由于Pool默认大小是CPU的核数，所以

## 子进程： 很多时候子进程并不是自身，而是一个外部的进程，创建子进程后还需要控制器输入和输出。

import subprocess
print('nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org']) # 创建子进程，并执行一个命令
print('Exit code:',r)

## 如果子进程需要输入内容，使用communicate()输入

import subprocess
print("$ nslookup")
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')# 相当于在命令行执行 nslookup，再手动输入参数
print(output.decode('utf-8'))
print('Exit code:',p.returncode)

## 进程间通信

from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print('Process to write:%s'%os.getpid())
    for v in ['A','B','C','D']:
        print('Put %s to queue...'%v)
        q.put(v)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s'%os.getpid())
    while True:
        v = q.get(True)
        print('Get %s from queue.'%v)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

# 多线程

## python的多线程是真正的Posix Thread ，而不是模拟出来的线程。
# 标准库提供两个模块 _thread 和 threading
# _thread是低级模块，threading是高级模块，对_thread进行了封装。大多数只需要用 threading模块

import time,threading

def loop():
    print('process %s is running ...'%threading.current_thread().name)
    n = 0
    while n < 3:
        n = n+1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.'%(threading.current_thread().name))

print('thread %s is running...'%threading.current_thread().name)

t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread %s ended.'% threading.current_thread().name)


# Lock

# 进程中，各自保留一份变量，互不影响。
# 线程，共享一份变量，互相影响。所以，多线程多线程中同时修改一个变量，会把内容改乱。
import time,threading
balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# 如果是单线程，balanc=0 ，究其原因是，cpu在执行简单语句时也是分开执行的
# balance = balance + n ==> x = balance + n   balance = x
# 这时候就需要引出锁的概念，保住一个线程在修改变量时，其他线程不能修改。这里不用进程的原因是，进程资源开销大

import threading
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            # 修改，这个时候其他线程不能获取锁
            change_it(n)
        finally:
            # 修改完后释放锁
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

while True:
    x = 0

'''
Python 解释器执行代码时，有一个GIL锁（Global Interpreter Lock）,任何python线程执行前，必须获取GIL锁。
每执行100条字节码，解释器自动释放GIL锁。让别的线程有机会执行。
实质上时将所有线程执行的代码都上了锁，所以多线程在Python中只能交替执行，即使100个线程也只能用到1个核。

所以，可以使用多线程，但只能利用一个核。

如果一定要用多线程利用多线程：
1. C语言扩展实现。
2. 使用多进程，每个进程独享一个GIL锁，相当于再开一个python解释器。
3. 重写一个不带GIL锁的解释器。
'''

# ThreadLockal
'''
每个线程使用自己局部变量，就不会影响其他线程。但是传递起来会比较麻烦。
'''
class Student:
    def __init__(self,name, *args, **kwargs):
        self.name = name
def std_thread(name):
    std = Student(name)
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    print(std.name)
    std.name = 'b'
def do_task_2(std):
    print(std.name)
std_thread('a')
# 这样写，一层一层传递肯定会出现问题，前面方法修改了，由于是局部变量，多个线程修改肯定会出现问题。如果用全局变量传递到线程中就是引用，变成局部变量不能共享。
# 如果把对象放到一个字典中，通过字典获取，就可以了。
import threading
glob_dic = {}
class Student:
    def __init__(self,name,*args, **kwargs):
        self.name = name
def std_thread(name):
    std = Student(name)
    glob_dic[threading.current_thread()] = std
    do_task_1()
    do_task_2()
def do_task_1():
    std = glob_dic[threading.current_thread()]
    print('task_1:',std.name)
    std.name = 'a'
    print('task_1:',std.name)
def do_task_2():
    std = glob_dic[threading.current_thread()]
    print('task_2:',std.name)
    std.name = 'b'
    print('task_2:',std.name)
std_thread('c')

# ThreadLocal 的使用
import threading
class Student:
    def __init__(self,name,*args, **kwargs):
        self.name = name
local_scool = threading.local() # 创建全局的ThreadLocal对象
def process_student():
    std = local_scool.student # 获取当前线程关联的student

def process_thread(name):
    local_scool.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()