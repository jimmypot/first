#有时候让进程有一个有可读性的名字会更好。幸运的是，Process 类支持给进程命名。让我们来看一下

import os

from multiprocessing import Process, current_process #从多进程模块中导入process与current_process类

def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc_name = current_process().name    #multiprocessing 模块默认为每一个进程的名字指派了一个数字 如Process-1
    print('{0} doubled to {1} by: {2}'.format(
        number, result, proc_name))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))  #再生成5个进程
        procs.append(proc)   #为了后面的join而做铺垫
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))  #生成一个有名字Test的进程
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()

