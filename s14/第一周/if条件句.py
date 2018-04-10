'''1'''
'''
if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else

if语句的完整形式为：
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>


场景一、用户登陆验证

# 提示输入用户名和密码  
# 验证用户名和密码
#     如果错误，则输出用户名或密码错误
#     如果成功，则输出 欢迎，XXX!
 
#!/usr/bin/env python
# -*- coding: encoding -*-  
import getpass 
 
name = raw_input('请输入用户名：')
pwd = getpass.getpass('请输入密码：')
  
if name == "alex" and pwd == "cmd":
    print("欢迎，alex！")
else:
    print("用户名和密码错误")
'''