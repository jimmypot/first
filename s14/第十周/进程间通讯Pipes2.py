from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello from child'])
    conn.send([42, None, 'hello from child2'])
    print("from parent:",conn.recv())
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()   #生成一个管道实例
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())
    print(parent_conn.recv())
    parent_conn.send("张洋可好")
    p.join()  #也可以用p.terminate() 结束子管道进程