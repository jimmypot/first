'''1'''
'''
>>>集合

集合是一个无序的，不重复的数据组合，它的主要作用如下：
去重，把一个列表变成集合，就自动去重了
关系测试，测试两组数据之前的交集、差集、并集等关系

'''

list_1 = [1,2,4,5,7,3,6,7,9]
list_1 = set(list_1)
print(list_1,type(list_1))

list_2 = set([4,2,6,0,66,22,8])
print(list_1,list_2)
list_1.intersection(list_2)    #交集
print(list_1.intersection((list_2)))

print(list_1.union(list_2))   #并集

print(list_1.difference(list_2))  #差集

print(list_1.issubset(list_2))    #判断是不是子集
list_3 = set([1,3,7])
print(list_1.issuperset(list_3))

print(list_1.symmetric_difference(list_2))  #对称差集

list_4 = set([5,9,8])
print(list_3.isdisjoint((list_4)))          #判断是否有交集，如果没有，则返回True

#运算符

print(list_1 & list_2)  #交集
print(list_2 | list_1)  #并集
print(list_1 - list_2)  #in list_1 not in list_2
print(list_1 ^ list_2)  #对称差集


#基本操作：

list_1.add(999)    #添加一项
print(list_1)

list_1.update([999,88,7,89])  #添加多项
print(list_1)






