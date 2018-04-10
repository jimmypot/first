'''
123
'''

'''
1、编码解码是怎么一回事？

Python 里面的编码和解码也就是 unicode 和 str 这两种形式的相互转化。

编码是 unicode -> str，相反的，解码就是 str -> unicode。

str形式，也就是字符串形式都是以一定的编码格式存在的，常见的编码格式有utf-8、ASCII、gb2312,gbk等等。

str1.decode(‘gb2312’)，表示将gb2312编码的字符串str1解码成unicode。

str2.encode(‘utf-8’)，表示将unicode字符串str2转换成用utf-8格式编码的字符串。

不同编码格式的字符串之间相互转换编码格式的话，都要先解码成unicode，再编码成其他编码格式的字符串。就拿上面的str1来说，
将str1转成utf-8编码的字符串，需要这么做： 
str1.decode(‘gb2312’).encode(‘utf-8’)。

2、如何在python文件中指定编码、解码格式呢

我们在编写python脚本的时候，通常在#! /usr/bin/env python下面一行指定该py文件的默认编码格式。
比如# coding=utf-8，表示该py文件中的字符串都是以utf-8格式编码的。

而sys.defaultencoding则指明了默认的字符串解码方式。在解码时没有明确指明解码方式的时候使用。

还要记住一点，字符串用什么格式编码，就要用相同的格式解码才能变成unicode。

3、编码解码格式要一致

#! /usr/bin/env python
# -*- coding: utf-8 -*-
s = '中文'  # 这里的 s 是utf-8编码的字符串类型
s.encode('gb18030')

观察上面的代码，我们预计会报错误。
因为第二行指定了该py文件里面的字符串默认编码格式是utf-8的，所以s这个字符串就是utf-8编码的字符串。

对于这种情况，我们有两种方法来改正错误：
一是明确的指示出 s 的解码方式

#! /usr/bin/env python
# -*- coding: utf-8 -*-
s = '中文'
s.decode('utf-8').encode('gb18030')  #先将以utf-8编码的s解码成unicode,然后将其再编码成gb18030

二是更改 sys.defaultencoding 为文件的编码方式

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

str = '中文'
str.encode('gb18030')

这里在调用sys.setdefaultencoding(‘utf-8’) 设置默认的解码方式之前，执行了reload(sys)，这是必须的，
因为python在加载完sys之后，会删除 sys.setdefaultencoding 这个方法，
我们需要重新载入sys，才能调用 sys.setdefaultencoding 这个方法。

具体接着看http://www.cnblogs.com/evening/archive/2012/04/19/2457440.html
以及http://blog.csdn.net/liuchunming033/article/details/52223612
'''
import sys
print(sys.getdefaultencoding())
msg = '我爱北京天安门'
msg_gb2312 = msg.encode('gb2312')
gb2312_to_unicode = msg_gb2312.decode('gb2312')
gb2312_to_utf8 = msg_gb2312.decode('gb2312').encode('utf-8')

print(msg)
print(msg_gb2312)
print(gb2312_to_unicode)
print(gb2312_to_utf8)

import sys
f = open("a",'r',encoding='utf-8')

with open('a','r',encoding = 'utf-8') as f:
    for line in f:
        print(line)

