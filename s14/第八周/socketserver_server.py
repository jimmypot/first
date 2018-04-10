import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handel(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{}wrote：'.format(self.client_address[0]))
                print(self.data)
                self.request.sendall(self.data.upper())
            except ConnectionResetError as e:
                print('error',e)
                break

if __name__ =='__main__':
    HOST,PORT = 'localhost',9999
    #创建一个服务，将localhost绑定到9999端口
    server = socketserver.TCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()