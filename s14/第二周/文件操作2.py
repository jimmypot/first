f = open('yesterday2',"r",encoding="utf-8")  #文件句柄
'''
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
'''
#for i in range(5):
 #   print(f.readline())

#print(f.readlines())
'''
#low循环
for index,line in enumerate(f.readlines()):
    if index ==9:
        print("------我是分割线-----")
        continue
    print(line.strip())

count = 0
for line in f:
    if count ==2:
        print("------我是分割线-----")
        count += 1
        continue
    print(line)
    count +=1
'''
f = open("yesterday2",'r',encoding='utf-8')
print(f.tell())
print(f.readline(25))
print(f.tell())
f.seek(0)
print(f.read())

print(f.fileno())


#进度条
'''import sys,time
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.1)
'''
f = open("yesteday2","w+",encoding="utf-8")   #写读操作
f = open("yesterday2",'r+',encoding="utf-8")   #读写操作
f = open("yesterday2",'a+',encoding="utf-8")   #追加读写操作
f = open("yesterday2",'rb',encoding="utf-8")   #二进制文件读操作
f = open("yesterday2",'+',encoding="utf-8")   #二进制读操作
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("------diao------")
print(f.read())