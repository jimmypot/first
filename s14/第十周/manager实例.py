from multiprocessing import Process, Manager
import os

def f(d, l):
    d[os.getpid()] =os.getpid()   #字典的键和值都是进程ID
    l.append(os.getpid())    #l是进程ID列表
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() #{} #生成一个字典，可在多个进程间共享和传递,类似于字典生成器

        l = manager.list(range(5))#生成一个列表，可在多个进程间共享和传递 ，类似于列表生成器
        p_list = []
        for i in range(10):   #生成十个进程
            p = Process(target=f, args=(d, l))
            p.start()    #运行该进程
            p_list.append(p)    #p_list是进程列表，为join方法埋下伏笔
        for res in p_list: #等待结果
            res.join()

        print(d)

