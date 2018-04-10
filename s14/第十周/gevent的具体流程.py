#Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是Greenlet,它会自动调度那些未完成的协程。
#它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('Explicit context switch to foo again')
def bar():
    print('Explicit context to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar')
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")

#”gevent.joinall()”方法会等待所有传入的greenlet协程运行结束后再退出，这个方法可以接受一个”timeout”参数来设置超时时间，
gevent.joinall([
    gevent.spawn(foo),    # ”gevent.spawn()”方法会创建一个新的greenlet协程对象，并运行它。
    gevent.spawn(bar),
    gevent.spawn(func3),
])