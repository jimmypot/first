#生成协程实例对象

from greenlet import greenlet

def one():
    print(12)
    gr2.switch()   #使用greenlet对象的switch()方法，即可以切换协程,此处跳转到two()函数中的对应下一步骤
    print(34)
    #gr2.switch()

def two():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(one)   #这里创建了两个协程对象，分别对应于函数one()和two()。
gr2 = greenlet(two)
gr1.switch()

'''上例中，我们先调用”gr1.switch()”，函数test1()被执行，然后打印出”12″；接着由于”gr2.switch()”被调用，
协程切换到函数test2()，打印出”56″；之后”gr1.switch()”又被调用，所以又切换到函数test1()。
但注意，由于之前test1()已经执行到第5行，也就是”gr2.switch()”，所以切换回来后会继续往下执行，也就是打印”34″；
现在函数test1()退出，同时程序退出。由于再没有”gr2.switch()”来切换至函数test2()，所以程序第11行”print 78″不会被执行。'''

