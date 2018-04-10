import socket,sys
client = socket.socket()
client.connect(('localhost',9999))
while True:
    msg = input(">>>>").strip()
    if len(msg)==0:
        continue
    client.send(msg.encode('utf-8'))
    res_return_size = client.recv(1024) #接收的命令结果的大小
    print('接收的数据的大小：',res_return_size)
    total_res_size = int(res_return_size)
    print('数据总量大小：',total_res_size)
    client.send('准备好接收了，请发送'.encode('utf-8'))
    received_size = 0 #已接收到的数据
    cmd_res = b''
    f = open('test_copy.html','wb') #把接收到的数据结果存下来，等待接下来的校验
    while received_size != total_res_size:
        data = client.recv(1024)
        received_size += len(data) #注意实际收到的数据可能比1024要少
        cmd_res += data
    else:
        print("数据接收完了",received_size)
        #print(cmd_res.decode())
        f.write(cmd_res)  #把接收到的数据存下来，等待校验
#print(data.decode())
    client.close()

