from gevent import monkey;monkey.patch_socket()#对socket标准库打上猴子补丁，此后socket标准库中的类和方法都会被替换成非阻塞式的
import gevent
import socket

urls = ['www.pronhub.com', 'www.gevent.org', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=5)

print([job.value for job in jobs])

'''
上述代码的第一行就是对socket标准库打上猴子补丁，此后socket标准库中的类和方法都会被替换成非阻塞式的，
所有其他的代码都不用修改，这样协程的效率就真正体现出来了。
Python中其它标准库也存在阻塞的情况，gevent提供了”monkey.patch_all()”方法将所有标准库都替换
from gevent import monkey; monkey.patch_all()
'''

