def foo():  #函数的嵌套
    print('in the foo')
    def bar():
        print('in the bar')
    bar()
foo()



