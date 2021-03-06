'''1'''
'''
》》》整数
int（整型）
　　在32位机器上，整数的位数为32位，取值范围为-2**31～2**31-1，即-2147483648～2147483647
　　在64位系统上，整数的位数为64位，取值范围为-2**63～2**63-1，即-9223372036854775808～9223372036854775807
long（长整型）
　　跟C语言不同，Python的长整数没有指定位宽，即：Python没有限制长整数数值的大小，但实际上由于机器内存有限，我们使用的长整数数值不可能无限大。
　　注意，自从Python2.2起，如果整数发生溢出，Python会自动将整数数据转换为长整数，所以如今在长整数数据后面不加字母L也不会导致严重后果了。
float（浮点型）
    先扫盲 http://www.cnblogs.com/alex3714/articles/5895848.html 
　　浮点数用来处理实数，即带有小数的数字。类似于C语言中的double类型，占8个字节（64位），其中52位表示底，11位表示指数，剩下的一位表示符号。
complex（复数）
　　复数由实数部分和虚数部分组成，一般形式为x＋yj，其中的x是复数的实数部分，y是复数的虚数部分，这里的x和y都是实数。
注：Python中存在小数字池：-5 ～ 257

》》》字符串
字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。请注意，''或""本身只是一种表示方式，不是字符串的一部分，
因此，字符串'abc'只有a，b，c这3个字符。
万恶的字符串拼接：
　　python中的字符串在C语言中体现为是一个字符数组，每次创建字符串时候需要在内存中开辟一块连续的空，
并且一旦需要修改字符串的话，就需要再次开辟空间，万恶的+号每出现一次就会在内从中重新开辟一块空间。

如果'本身也是一个字符，那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。
如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，
转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\。

》》》布尔值
布尔值和布尔代数的表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，
在Python中，可以直接用True、False表示布尔值（请注意大小写），也可以通过布尔运算计算出来：
布尔值可以用and、or和not运算。
'''