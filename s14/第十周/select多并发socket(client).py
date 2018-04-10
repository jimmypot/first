import socket,sys

messages = [ b'This is the message. ',
             b'It will be sent ',
             b'in parts.',
             ]
server_address = ('localhost', 9000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(1020)] #列表生成式
# Connect the socket to the port where the server is listening
print('connecting to %s port %s' % server_address)

for s in socks:     #将所有连接都连上服务端
    s.connect(server_address)

for message in messages:  #每个连接都发送三个数据
    for s in socks:
        print('%s: sending "%s"' % (s.getsockname(), message) )
        s.send(message)

    for s in socks:   #所有的连接都要接收数据
        data = s.recv(1024)
        print( '%s: received "%s"' % (s.getsockname(), data) )
        if not data:   #如果没有接收到数据，则表示当前连接任务已结束
            print(sys.stderr, 'closing socket', s.getsockname() )