import gevent

def task(pid):
    gevent.sleep(0.5)
    print('Task %s done' % pid)

def synchronous():     #生成十个进程
    for i in range(1, 10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]   #”gevent.spawn()”方法会创建一个新的greenlet协程对象，并运行它
    gevent.joinall(threads) #”gevent.joinall()”方法会等待所有传入的greenlet协程运行结束后再退出，这个方法可以接受一个”timeout”参数来设置超时时间。

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()