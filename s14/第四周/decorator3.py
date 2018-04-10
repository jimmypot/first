
import time

def timer(func):    #timer(testt1)  func testt1
    def deco1(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)   # 执行testt函数
        stop_time = time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return deco1

@timer    #testt1= timer（testt1）
def stestt1():
    time.sleep(3)
    print('in the stestt1')

@timer
def stestt2(name,age):
    print('stestt2：',name,age)

#test1 =timer(testt1)
stestt1()
stestt2('alex',24)


