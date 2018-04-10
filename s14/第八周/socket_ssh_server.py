#极简版ssh,客户端连接上服务器后，让服务器执行命令，并返回给客户端。
import socket
import os,subprocess
server = socket.socket()  #获得socket实例
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost',9999)) #绑定端口
server.listen() #开始监听
while True:
    print('等待客户端连接')
    conn,addr =server.accept() #接受并建立与客户端的连接
    print('新连接：',addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break #这里断开就会回到第一次外层的loop,break结束当前循环
        print('收到命令:',data)
        #res = os.popen(data.decode()).read() #popen只能接收str,而socket发送的是bytes,所以需要decode（）
        res = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE).stdout.read()
        if len(res) == 0:
            res = '命令执行成功，没有其他返回结果'.encode('utf-8')
        conn.send(str(len(res)).encode('utf-8'))  #发送数据前，先告诉客户端需要发送几次
        print('等待客户ack应答')
        client_final_ack = conn.recv(1024) #等待客户端响应
        print('客户应答：',client_final_ack.decode())
        print(type(res))
        conn.sendall(res.encode('utf-8'))  #这里使用sendall相当于循环调用send，直到数据发送完成

server.close()




