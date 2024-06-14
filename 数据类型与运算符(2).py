'''
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
'''


'''print('luck_number的数据类型是:', type(luck_number))
print(my_name, '的幸运数字是:', luck_number)'''
'''# Python动态修改变量的数据类型，通过赋不同类型的值就可以直接修改
luck_number = '北京欢迎你'
print('luck_number的数据类型是:', type(luck_number))'''


'''#在Python中允许多个变量指向同一个值
no = number = 1024 #no与number都指向了1024这个整数值print(no, number)
print(id(no))# id()查看对象的内存地址的
print(id(number))'''
'''十进制  无
二进制  0b或0B  由0和1组成
八进制  0o或0O  由0到7组成
十六进制  0x或0X  由0到9，a到f或A到F组成'''

'''num = 987# 默认是十进制，表示整数
num2 = 0b1010101#使用二进制表示整数
num3 = 0o765# 使用八进制表示整数
num4 = 0x87ABF# 使用十六进制表示整数
print(num)
print(num2)
print(num3)
print(num4)'''


'''x = 10
y = 10.0
print('x的数据类型:', type(x))# int
print('y的数据类型:', type(y))# float


x = 1099E1413
print('科学计数法:', x, 'x的数据类型:', type(x))
print(0.1+0.2)
print(round(0.1+0.2, 1))
x = 123+456j
print('实数部分:', x.real)
print('虚数部分:', x.imag)'''
'''
\n  换行符
\t  水平制表位，用于横向跳到下一个制表位
\"  双引号
\'  单引号
\\  一个反斜杠
'''
'''print('hello\tooo')
print('hell\toooooo')
print('hellooooooo')
print('老师说:\'好好学习，天天向上\'')
print('北\n京\n欢\n迎你')
print(r'北\n京\n欢\n迎你')
print(R'北\n京\n欢\n迎你')'''
'''s = 'HELLOWORLD'
print(s[0],s[-10]) # 序号9和序号-10表示的是同一个字符print('北京欢迎你'[4]) # 获取字符串中索引为4
print('北京欢迎你'[-1])
print(s[2:7])#从2开始到7结束不包含7，正向递增
print(s[-8:-3])#反向递减
print(s[:5])# 默认N从B开始
print(s[5:]) #M 默认是切到字符串的结局'''


'''x = '2022年'
y = '北京冬奥会'
print(x+y)#连接两个字符
print(x*10)#对x这个字符串的内容复制10次
print(10*x)
print('北京' in y)
print('上海' in y)'''


'''x = True
print(x)
print(type(x))
print(x+10)
print(False+10)
print(bool(False))
print(bool(None))'''


'''x = 10
y = 3
z = x/y
print(z, type(z))
print('float类型转成int类型:', int(3.14))
print('float类型转成int类型:', int(3.9))
print('float类型转成int类型:', int(-3.14))
print('float类型转成int类型:', int(-3.9))
print('int类型转成float类型:', float(10))'''
'''print(int('100')+int('200'))
print(int('18a'))
print(int('3.14'))
print(float('45a.987'))
print(ord('杨'))
print((chr(26472)))
print('十进制转成十六进制:', hex(26472))
print('十进制转成八进制:', oct(26472))
print('十进制转成二进制:0', bin(26472))'''


'''s = '3.14+3'
print(s, type(s))
x = eval(s)
print(x, type(x))'''


'''age = eval(input('请输入您的年龄:'))
print(age, type(age))
height = eval(input('请输入您的身高:'))
print(height, type(height))'''


'''hello = '北京欢迎你'
print(hello)
print(eval('hello'))
print(eval('北京欢迎你'))'''
'''print('加法:', 1+1)
print('减法:', 1-1)
print('乘法:', 2*3)
print('除法:', 10/2)
print('整除:', 10//3)
print('取余:', 10%3)
print('幂运算:', 2**4)
print(10/0)'''
'''x = 20
y = 10
x = x+y
print(x)#30
x += y#40  相当于x=x+y
x -= y#30 相当于x=x-y
print(x)
x *= y
print(x)
x /= y
print(x)
print(type(x))
x %= 2
print(x)
z = 3
y //= z
print(y)
y **= 2
print(y)'''
'''a = b = c = 100
print(a, b, c)
a, b = 10, 20
print(a, b)
print('-----如何交换两个变量的值呢？-----')
a, b = b, a
print(a, b)
print('98大于90吗？', 98 > 90)
print('98小于90吗？', 98 < 90)
print('98等于90吗？', 98 == 90)
print('98不等于90吗？', 98 != 90)
print('98大于等于98吗？', 98 >= 98)
print('98小于等于98吗？', 98 <= 98)'''
'''print(True and True)
print(True and False)
print(False and False)
print(False and False)
print('-' * 40)
print(8 > 7 and 6 > 5)
print(8 > 7 and 6 < 5)
print(8 < 7 and 10 / 0)
print('-' * 40)
print(True or True)
print(True or False)
print(False or False)
print(False or True)
print('-' * 40)
print('按位与运算:', 12 & 8)
print('按位或运算:', 4 | 8)
print('按位异或运算符:', 31 ^ 22)
print('按位取反:', ~ 123)'''
print('左移位:', 2 << 2)
print('左移位:', 2 << 3)
print('右移位:', 8 >> 2)
print('右移位:', -8 >> 2)



