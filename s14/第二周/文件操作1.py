'''1'''
'''文件操作
对文件操作流程
打开文件，得到文件句柄并赋值给一个变量
通过句柄对文件进行操作
关闭文件 

》》》基本操作　　

f = open('lyrics') #打开文件
first_line = f.readline()
print('first line:',first_line) #读一行
print('我是分隔线'.center(50,'-'))
data = f.read()# 读取剩下的所有内容,文件大时不要用
print(data) #打印文件
f.close() #关闭文件

》》》打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a
"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U
"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

rb
wb
ab

》》》with语句

为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log','r') as f:    
    ...
如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。

在Python 2.7 后，with又支持同时对多个文件的上下文进行管理，即：

with open('log1') as obj1, open('log2') as obj2:
    pass
'''
#data = open('yesterday2',encoding='utf-8').read()  #打开文件，并且读取文件，存储于"data"中
f = open('yesterday2',"w",encoding="utf-8")  #文件句柄
#data = f.read()
#data2 = f.read()

#print(data)
#print("------data2------",data2)
f.write("when i was young i listen to the radio\n",)
f.write("天安门上太阳升"
        ",\n")


#a = append 追加, w = 写操作，r = 读操作
f = open('yesterday2',"a",encoding="utf-8")  #文件句柄
f.write("我爱北京天安门.......,\n",)
f.write("天安门上太阳升.......。")


#写操作
f = open("yesterday3","w+",encoding="utf-8")
f.write("----------叼----------\n")
f.write("----------叼----------\n")
f.write("----------叼----------\n")
f.write("----------叼----------\n")
f.seek(10)
print(f.tell())
print(f.readline())
f.write("------这句写在哪儿了呢？------")
f.close()

