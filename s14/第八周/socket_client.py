#为了测试上面这个服务器，编写一个客户端程序
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('localhost',9999))
#接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
    s.send(data)  #发送数据
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()


'''
小结
用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，
然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。
'''