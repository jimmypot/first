from greenlet import greenlet

def tes1():
    print(11)
    try:
        gr2.throw(NameError)   #另外，我们可以通过greenlet对象的”throw()”方法，手动往一个协程里抛个异常
        gr2.switch()           #子协程的异常会被抛到这里，因为值协程是从这儿引进的
    except NameError:
        print(12)              #此时异常被捕获，并且打印69
    print(13)
    gr3.switch()

def tes2():
    print(21)
    raise NameError           #如果”gr2″的父协程是”gr1″的话，异常先回抛到函数test1()的代码”gr2.switch()”处。

#有一个异常是特例，不会被抛到父协程中，那就是”greenlet.GreenletExit”，这个异常会让当前协程强制退出。
def tes3():
    print(31)
    raise greenlet.GreenletExit    #此时tes3就此终止
    print(32)   #代码行”print（78）″永远不会被执行。但这个异常不会往上抛，所以其父协程还是可以正常运行。

gr1 = greenlet(tes1)
gr2 = greenlet(tes2, gr1)
gr3 = greenlet(tes3,gr1)
gr1.switch()
print(91)

