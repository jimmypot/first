import threading,time

def run(n):
    print('task',n)
    time.sleep(3)
    print('task done',n)

def run2(n):
    print('task',n)
    print('task done',n)

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.setDaemon(True) #把当前线程设置为守护线程（当非守护线程结束时，程序结束，不会考虑守护线程结束与否）
    t.start()
    t_objs.append(t)
    print(t.getName())


#for m in t_objs:
#    m.join()      #join函数：等待该函数全部结束后，程序才接着向下走。

print('---------all the threads have finfshed')  #这个主线程结束后，整个程序结束，不管之前的守护线程是否结束
print('cost:',time.time()-start_time)      #这个主线程结束后，整个程序结束，不管之前的守护线程是否结束
gg = threading.Thread(target=run2,args=(3,))  #这个主线程结束后，整个程序结束，不管之前的守护线程是否结束
gg.start()                                 #这个主线程结束后，整个程序结束，不管之前的守护线程是否结束
