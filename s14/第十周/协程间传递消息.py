from greenlet import greenlet

def tes1():
    print(12)
    y = gr2.switch('aa')    #此时 返回得到y = 'bb'
    print(y)

def tes2(x):   #此时x = 'aa'
    print(x)
    gr1.switch('bb')
    print(78)     #此行不会执行

gr1 = greenlet(tes1)
gr2 = greenlet(tes2)
gr1.switch()

'''
在test1()中调用”gr2.switch()”，由于协程”gr2″之前未被启动，所以传入的参数”56″会被赋在test2()函数的参数”x”上；
在test2()中调用”gr1.switch()”，由于协程”gr1″之前已执行到第5行”y = gr2.switch(56)”这里，
所以传入的参数”34″会作为”gr2.switch(56)”的返回值，赋给变量”y”。这样，两个协程之间的互传消息就实现了。
'''