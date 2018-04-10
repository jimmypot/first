#使用方法跟threading里的queue(队列)差不多

from multiprocessing import Process, Queue
import os
import time
import random

# '写数据'进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in range(50):
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(0.1)

# '读数据'进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)

#只要Queues中有数据，则get数据，没有数据的话则等待put方法写入数据
if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()    #当put完所有的数据后 ，停止put线程
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()  #put线程停止后，紧接着停止get线程
