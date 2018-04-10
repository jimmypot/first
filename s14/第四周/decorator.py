#装饰器的举例
import time

def bar():
    time.sleep(3)
    print("in the bar")
def jimmytest2(func):
    print(func)
    return func

#print(jimmytest2(bar))
bar = jimmytest2(bar)
bar()


