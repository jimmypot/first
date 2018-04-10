from greenlet import greenlet

def tes1():
    print(12)
    gr2.switch()
    print(34)

def tes2():
    print(56)

gr1 = greenlet(tes1)
gr2 = greenlet(tes2, gr1)  #这里创建greenlet对象”gr2″时，指定了其父协程是”gr1″。
# 所以在函数tes2()里，虽然没有”gr1.switch()”代码，但是在其退出后，程序一样回到了函数tes1()，并且执行”print 34″
gr1.switch()
print(78)  #同样，在tes1()退出后，代码回到了主程序，并执行”print (78)″。

#注意-----协程退出后，就无法再被执行了。如果上例在函数test1()中，再加一句”gr2.switch()”，
# 运行的结果是一样的。因为第二次调用”gr2.switch()”，什么也不会运行。