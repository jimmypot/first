#装饰器举例
import time
def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):    # 不是装饰器，因为调用方式改变了
    start_time = time.time()
    func()    #run bar
    stop_time = time.time()
    print('the func run time is %s'%(stop_time-start_time))
func = bar()
#test1(bar)
bar()

