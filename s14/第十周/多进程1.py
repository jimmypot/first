import os

from multiprocessing import Process


def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

'''
在这个例子中，我们导入了 Process ，并创建一个 doubler 函数。在这个函数中，我们将传入的数字扩大二倍。
我们还用 Python 中的 os 模块得到当前进程的ID（或者说 pid）。这可以告诉我们哪个进程正在调用函数。
代码底部的那个循环中，我们创建了一系列进程并启动它们。最下边的那个循环在每一个进程上调用了 join() 方法，
它将告诉 Python 等待进程结束。如果你需要结束一个进程，你可以调用它的 terminate() 方法。
'''