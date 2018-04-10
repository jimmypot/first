'''1'''
'''
》》变量定义的规则：

变量名只能是 字母、数字或下划线的任意组合
变量名的第一个字符不能是数字
以下关键字不能声明为变量名
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or',
 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
'''
》》全局与局部变量

在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
当全局变量与局部变量同名时：
在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。
'''

school = 'Oldboy edu'

def change_name(name):               #里面定义的是局部变量，只在函数内部有效
    global school                    #当在函数内部声明，将变量声明成全局变量时，该变量变成全局变量
    school = 'Mage linux'
    print('before the change :',name,school)
    name = 'Alex li '                      #这个函数就是这个变量的作用域
    print('after the change ：',name)

name = 'alex'
change_name(name)
print(name)
print(school)



