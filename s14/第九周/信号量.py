import threading, time

def run(n):
    semaphore.acquire()  #调用acquire时计数器-1
    time.sleep(2.5)
    print("run the thread: %s\n" % n)
    semaphore.release()   #调用release时计数器+1

num = 0
semaphore = threading.BoundedSemaphore(2)  # 最多允许5个线程同时运行
for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()

while threading.active_count() != 1:
    pass
    # print(threading.active_count())
else:
    print('----all threads done---')
    #print(num)