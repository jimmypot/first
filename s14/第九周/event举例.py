import time,threading

event = threading.Event()

def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("\033[41;1mred light is on....\033[0m")   #显示红灯状态
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on....\033[0m")   #在count在（0,5）时显示绿灯状态
        time.sleep(1)
        count +=1

def car(name):
    while True:
        if event.is_set(): #如果是绿灯状态，则汽车通行
            print("朱俊的[%s] running..."% name )
            time.sleep(1)
        else:         #如果是红灯状态，则当前进程挂起等待，直到标志位为真
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)

#红绿灯开始运行
light = threading.Thread(target=lighter,)
light.start()

#实例化汽车对象
car1 = threading.Thread(target=car,args=("Tesla",))
time.sleep(3)
car2 = threading.Thread(target=car,args=("奇瑞QQ",))

#汽车开始行驶
car1.start()
car2.start()
