from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    while True:
        print(conn.recv())

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()   #生成一个管道实例
    p = Process(target=f, args=(child_conn,))  #实例化一个子管道进程
    p.start()   #子管道开始启动，并向父管道发送数据
    print(parent_conn.recv())   # 父管道收到并打印数据
    parent_conn.send('666')  #父管道发送数据
    p.terminate()            #结束子管道进程

