''''''
'''在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

为什么要使用生产者和消费者模式
在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，时常发生生存者和消费者不处于均衡状态的时候
为了解决这个问题于是引入了生产者和消费者模式。

什么是生产者消费者模式
生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，
而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，
而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。

下面来学习一个最基本的生产者消费者模型的例子'''

import threading,time
import queue

q = queue.Queue(maxsize=10)

#每隔一定时间生产一个骨头（向队列中Put一个元素）
def Producer(name):
    count = 1
    while True:
        q.put("骨头%s" % count)
        print("生产了骨头",count)
        count +=1
        time.sleep(0.6)


#每隔一定时间消费掉一个骨头
def  Consumer(name):
    #while q.qsize()>0:
    while True:
        print("[%s] 取到[%s] 并且吃了它..." %(name, q.get()))
        time.sleep(1)


#创建一个生产者与两个消费者
p = threading.Thread(target=Producer,args=("Alex",))
c = threading.Thread(target=Consumer,args=("ChengRonghua",))
c1 = threading.Thread(target=Consumer,args=("王森",))

#开始运行模型
p.start()
c.start()
c1.start()