from multiprocessing import Process, Lock
import time

def printer(item, lock):
    lock.acquire()  #这样用锁 ，相当于串行过程
    try:
        print(item)
        time.sleep(2)
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = ['tango', 'foxtrot', 10]
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()

'''
这里我们创建了一个函数直接打印传递过来的任何东西。为了防止线程被其他事情干扰，我们用了一个 Lock 对象。
这段代码将遍历我们列表中的三项内容，并分别为其创建一个进程。每个进程都会调用该函数，并将可迭代对象中的一个元素传入函数。
因为我们用了锁，所以后边的进程将会等到锁释放之后才会继续执行
'''



