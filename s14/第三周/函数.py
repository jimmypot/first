'''1'''
'''
定义: 函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可

特性:
减少重复代码
使程序变的可扩展
使程序变得易维护

语法定义
>>>在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
def sayhi():#函数名
    print("Hello, I'm nobody!")
sayhi() #调用函数
可以带参数

!!!请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。
因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。return None可以简写为return

Python内置了很多有用的函数，我们可以直接调用。
要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。
可以直接从Python的官方网站查看文档：
http://docs.python.org/3/library/functions.html#abs
也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
'''
def func1():    #定义一个函数
    "testing"
    print('in the func1')  #代表复杂的逻辑
    return 0


def func2():   #定义一个过程
    '''testing2'''
    print('in the func2')
#过程是没有返回值的函数

x = func1()
y = func2()
print('from func1 return is %s'%x)
print('from func2 return is %s'%y)

def text3():
    print('in the text3')
    return 1,['nibchb'],{'jkcbjkj'},'cwbhjch'  #实际上返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format) #当下时间输出
    with open("a.txt",'a+')as f:
        f.write('%s end action\n'%time_current)

def text1():
    print("in the test1")
    logger()
def text2():
    print("in the test2")
    logger()
def text3():
    print("in the test3")
    logger()

text1()
text2()
text3()