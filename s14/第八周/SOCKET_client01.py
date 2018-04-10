#client

import socket
client = socket.socket()   #声明socket类型，同时生成socket连接对象

client.connect(('localhost',9999))
client.send(b'hello world') #要求发送比特流型数据
data = client.recv(1024)
print('recv:',data)

client.close()
