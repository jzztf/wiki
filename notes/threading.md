# 线程操作

参考:@MorvanZhou

- 创建线程实例

`added_thread = threading.Thread(target=thread_job)`

- 开始线程

`added_thread.start()`

- 维护线程

`added_thread.join()`

- 线程属性
  - 查看当前线程:`threading.current_thread()`
  - 查看线程列表:`threading.enumerate()`
  - 所有线程数:`threading.active_count()`

```python
# 线程简单练习

import threading,time

def T_job():
    print("T start\n")
    for i in range(10):
        time.sleep(0.2)
    print("T finish\n")
    
def T2_job():
    print("T2 start\n")
    for i in range(10):
        time.sleep(0.2)
    print("T2 finish\n")
    
def main():
    # 定义线程
    T = threading.Thread(target=T_job,)
    T2 = threading.Thread(target=T2_job,)
    # 开始线程
    T.start()

    T2.start()
    T.join()
    T2.join()
    print("all done")
    
main()
```


- 队列操作, 交换数据

多线程是没有返回值的,如果需要返回函数的返回值,则需要使用queue

```python
import threading
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    #return l 无效
    # 将计算后的列表放到q中
    q.put(l)

def multithreading():
    # 创建队列实例
    q = Queue()
    threads = []
    data = [[1,2,3],[4,5,6],[7,8,9],[2,3,4]]
    # 创建4个线程
    for i in range(4):
        # 创建线程实例,将一个二位数组分成四次运行
        t = threading.Thread(target=job,args=(data[i],q))
        # 启动线程
        t.start()
        # 将线程添加到threads列表中
        threads.append(t)
    for thread in threads:
        # 将分线程加入到主线程中,完成每个线程后,才可以继续以后的命令,才可以返回值
        thread.join()
    results=[]
    for _ in range(4):
        # 循环四次, 每次都从q中拿出一个
        # q对象队列就是先进先出(FIFO)
        results.append(q.get())
    print(results)

multithreading()
```

- GIL

python全局管理, 使用多线程并不一定能够提升理想的效率

如果两个线程分工于不同的功能, 可能效率会提高很多, 如果运算的线程相关性较高, 也可能不是那么快

- lock

线程1拿到一个数据, 用来给第二个线程使用,就需要将线程1运行完后,锁起来

```python
import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1',A)
    lock.release()
        
def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2',A)
    lock.release()

lock = threading.Lock()
A = 0
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()
t1.join()
t2.join() 
```