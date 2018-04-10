import gevent
import socket

urls = ['www.pronhub.com', 'www.gevent.org', 'www.python.org']

#我们通过协程分别获取三个网站的IP地址，由于打开远程地址会引起IO阻塞，所以gevent会自动调度不同的协程。
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=5)
#我们可以通过协程对象的”value”属性，来获取协程函数的返回值。
print([job.value for job in jobs])
