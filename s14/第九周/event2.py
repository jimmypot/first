import threading

def do(event):
    print('start')
    event.wait()   #直到event的信号位为真时，才继续执行下去，否则阻塞当前该进程
    print('execute')

event_obj = threading.Event()   #实例化一个Event
inp = input('输入内容:')
if inp == 'true':
    event_obj.set()
for i in range(10):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()
