import threading, time

def run1():
    print("grab the first part data")
    lock.acquire()
    global num
    num += 1
    lock.release()
    return num

def run2():
    print("grab the second part data")
    lock.acquire()
    global num2
    num2 += 1
    lock.release()
    return num2

#在一次线程中同时调用run1与run2，并用线程锁进行每次操作，保证两个函数同步进行
def run3():
    lock.acquire()
    res = run1()
    print('--------between run1 and run2-----')
    res2 = run2()
    lock.release()
    print(res, res2)

num, num2 = 0, 0
lock = threading.RLock()  #获得一个递归锁
for i in range(10):
    t = threading.Thread(target=run3)
    t.start()

#打印当前的线程数目
while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('----all threads done---')
    print(num, num2)