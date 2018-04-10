#线程的调用方式---直接调用，给构造函数传递回调对象
#mthread=threading.Thread(target=xxxx,args=(xxxx))
#mthread.start()
import threading,time

def run(num): #定义每一个线程要运行的函数
    print('task',num)
    time.sleep(1)
def walk(foot):
    print("朱俊在用第%s只脚走路"%foot)
t1= threading.Thread(target=run,args=('t1',)) #生成一个线程实例，target指向需要运行的函数，args是该函数的参数数组
t2= threading.Thread(target=walk,args=('3',))

t1.start()   #启动线程
t2.start()

print(t1.getName()) #获取线程名
print(t1.getName())



#线程调用---继承调用,派生类中重写了父类threading.Thread的run()方法，其他方法（除了构造函数)都不应在子类中被重写，
# 换句话说，在子类中只有_init_()和run()方法被重写。
import threading,time

class Mythread(threading.Thread):
    def __init__(self,n):
        super(Mythread,self).__init__()   #继承父类的初始化方法
        self.n  =  n

    def run(self):   #定义每个线程要运行的函数，必须用run这个函数名称
        print('task',self.n)
        time.sleep(1)

t1= Mythread('t1')
t2= Mythread('t2')

t1.start()   #start时调用我的类中的run函数
t1.join()  #waiting t1线程结束
t2.start()
