'''1'''
'''
列表是我们最以后最常用的数据类型之一，通过列表可以对数据实现最方便的存储、修改等操作

>>>列表
names = ['Alex',"Tenglan",'Eric']
通过下标访问列表中的元素，下标从0开始计数
>>> names[2]
'Eric'
>>> names[-1]
'Eric'
>>> names[-2] #还可以倒着取
'Tenglan'

>>>元组
元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能再修改，所以又叫只读列表。
语法
names = ("alex","jack","eric")
它只有2个方法，一个是count,一个是index，完毕。


>>>字典
字典一种key - value 的数据类型，使用就像我们上学用的字典，通过笔划、字母来查对应页的详细内容。
语法:
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
字典的特性：
dict是无序的
key必须是唯一的,so 天生去重

循环dict 
复制代码
#方法1
for key in info:
    print(key,info[key])

#方法2
for k,v in info.items(): #会先把dict转成list,数据里大时莫用
    print(k,v)
'''

list_1 = ['尼玛','他玛','我玛']
list_1.remove(999)  #删除元素
print(list_1)

print(list_1.pop())
print(list_1.pop())

print(list_1.discard(88))


info  = {
    'stu1101' : 'tenglan wu',
    'stu1102' : 'longze luola',
    'stu1103' : 'xioaze maliya'
}
print(info)
print(info['stu1101'])
'''
info['stu1101'] = '武藤兰'
print(info)
del info['stu1101']
info.popitem()
info.pop('stu1103')
'''
print(info.get('stu1101'))


for i in info:
    print(i,info[i])

for k,v in info.items():
    print(k,v)

#学习网站
#多级列表
av_catalog={
    '欧美':{
        'www.youporn.com':['很多免费的，世界最大的','质量一般'],
        'www.pornhub.com':['很多免费的，也很大','质量比youporn高点'],
        'letmedothistoyou':['多是自拍，高质量很多','资源不多，更新慢'],
        'x-art.com':['质量很高','全部收费'] },
    '日韩':{'tokyo-hot':['质量一般','听说收费']},
    '大陆':{'1024':['全部免费，真好，好人一生平安','服务器在国外，慢']}
}
av_catalog['大陆']['1024'][1]='可以在国内做镜像'
print(av_catalog)