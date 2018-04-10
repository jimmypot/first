'''1'''
'''
列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>

创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4

我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
没有更多的元素时，抛出StopIteration的错误。
当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print(n)
...
0
1
4





'''
#a = [i*2 for i in range(10)]   #列表生成式
#c = (i*2 for i in range(10))   #列表生成器
'''
1-生成器只有调用时才会生成相应的数据
2-只记录当前位置
3-只有一个__next__()方法
'''
#c.__next__()    #依次按照顺序向下取

#斐布拉奇数列(函数生成器)
def fib(max):
    n,a,b = 0,0,1
    while n <max:
        #print(b)
        yield b
        a,b = b,a+b   #注：此处相当于 t=(b,a+b) ,t是一个trupe a= t[0] ,b=t[1]
        n +=1
    return 'done'

fib_gen = fib(10)
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
'''
这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
'''



'''-------------------------下面开始讲迭代器啦------------------------'''
'''
迭代器

我们已经知道，可以直接作用于for循环的数据类型有以下几种：一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。这些可直接作用于for循环的对象称为可迭代对象：Iterable.
可以使用isinstance()判断一个对象是否是Iterable对象：
>>> from collections import Iterable
>>> isinstance([], Iterable)
True
>>> isinstance({}, Iterable)
True
>>> isinstance(100, Iterable)
False

生成器不但可作用于for循环，还可被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
*可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False

生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True

为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

 小结
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

'''

