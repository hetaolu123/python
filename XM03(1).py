#课件三全部内容

#赋值运算符的顺序 从右到左
 # name='张三'
 # age=20
 # a=b=c=d=100#链式赋值
 # a,b,c,d='room'#字符分解赋值
 # print(a)
 # print(b)
 # print(c)
 # print(d)
 # print('---------输入/输出语句也是典型的顺序结构---------')
 # name=input('请输入您的姓名：')
 # age=eval(input('请输入您的年龄：'))
 # luck_number=eval(input('请输入您的幸运数字'))
 # print('姓名：',name)
 # print('年龄:',age)
 # print('幸运数字:',luck_number)

"""
number=eval(input('请输入您的6位中奖号码：'))
# 使用if语句
if number==987654:  #等值判断
    print('恭喜您，中奖了！')
if number!=987654:
    print('很遗憾，您未中本期大奖！')
"""

# print('-------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值类型-------')
# n=98 #赋值操作
# if n%2:
#     print(n,'是奇数')
# if not n%2:
#     print(n,'为偶数')
"""
print('---------判断一个字符串是否是空字符串----------')
x=input('请输入一个字符串：')
if x:
    print('x 是一个非空字符串')
if not x:
    print('x 是一个空字符串')
"""
# print('-------表达式也可以是一个单纯的布尔型变量-------')
# flag=eval(input('请输入一个布尔类型的值：True或Flase'))
# if flag:
#     print('flag的值为True')
#
# if not flag:
#     print('flag的值为Flase')
""" 
 print('-------使用if语句时，如果语句块中只有一句代码，可以将语句直接写在冒号的后面-------')
 a-18
 b=5
 if a>b:max=a #语句块中只有，赋最大值
 print('a和b的最大值为：',max)
"""

"""
score=eval(input('请输入您的成绩：'))
#多分支结构
if score<0 or score>100:
    print('成绩有误！')
elif 0<=score<60:
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')
"""

"""
answer=input('请问，你喝酒了吗？')
if answer=='y': #answer的值为y表示喝酒了
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('构不成酒驾，祝您一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车')
    else:
        print('喝酒不开车，开车不喝酒。行车不规范，亲人两行泪！')
else:
    print('你走吧，没你啥事儿！')
"""

"""
user_name=input('请输入您的用户名：')
pwd=input('请输入您的密码:')
if user_name=='ysj' and pwd=='888888':
    print('登录成功')
else:
    print('用户名或密码不正确')
"""

# score=eval(input('请输入您的成绩：'))
# if score<0 or score>100:
#     print('成绩无效')
# else:
#     print('您的成绩为：',score)

# score=input('请输入成绩等级：')
# match score:
#     case 'A':
#         print('优秀')
#     case 'B':
#         print('良好')
#     case 'C':
#         print('中等')
#     case 'D':
#         print('及格')
#     case 'E':
#         print('不及格')

# for i in 'hello':
#     print(i)
# for i in range(1,11):
#     if i%2==0:
#         print(i,'是偶数')
#  s=0
# for i in range(1,11):
#     s+=i
#     print('1~10之间的累加和为：',s)
"""
# (1)初始化变量
answer=input('今天要上课吗？y/n')
while answer=='y': #（2）条件判断
    print('好好学习，天天向上') # (3)语句块
    # (4)改变变量
answer=input('今天要上课吗？y/n')
"""

"""
# 1~100之间的累加和
s=0 # 存储累加和
i=1 # (1)初始化变量
while i<=100: # (2)条件判断
    s+=i    # (3)语句块
# (4)改变变量
    i+=1
else:
    print('1~100之间的累加和:',s)
"""

"""
# (1)初始化变量
i=0
while i<3:#（2）条件判断 0,1,2
    # (3)语句块
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码:')
    # 登录操作。if...else...
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登录，请稍后')
        # 需要改变循环变量，目的退出循环
        i=8  # 第三行判断i<3，8<3 False退出while循环
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1  # (4)改变变量
#单分支的判断
if i==3:# 当用户名或密码输入三次不正确的时候，循环执行结束了,i的最大值为3
print('对不起，三次均输入错')
"""

"""
for i in 'hello':
    if i=='e':
        break
    print(i)
print('--------------------')
for i in range(3):
    # (3)语句块
    user_name = input('请输入用户名:')
    pwd = input('请输入密码:')
    if user_name == 'ysj'and pwd =='888888':
        print('系统正在登录，请稍后...')
        break
    else:
        if i < 2:
            print('用户名或密码不正确,您还有',2-ì,'次机会')
else: # for...else
    print('三次均输入错误!')
"""

"""
s=0
i=1 #(1)初始化变量
while i <=100: #(2)条件判断
    # (3)语句块
    if i%2==1: # 奇数
        i+=1
        continue #不再执行后面的代码了
    # 累加求和的代码
    s+=i
    i+=1
print('1-100之间的偶数和:',s)
"""

"""
s=0
for i in range(1,101):
    if i%2==1:
        continue
        # 累加求和的代码
     s+=i
print('1-100之间的偶数和是:',s)
"""

# if True:
#     pass
# while True:
#     pass
# for i in range(10):
#     pass

#  章节习题
"""
实战一:
输入一个年份，判断是否是闰年
需求:从键盘获取一个四位的整数年份，判断其是否是闰年。
闰年的判断条件为:能被4整除但不能被100整除，或者能被
400整除。
#以下是运行代码：
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

# 获取用户输入
year = int(input("请输入一个四位整数年份: "))

# 判断是否为闰年
if is_leap_year(year):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

"""

"""
实战二:
模拟10086查询功能
需求:输入1，显示当前余额；输入2，显示当前的剩余流量，单位为G；
输入3，显示当前的剩余通话，单位为分钟;输入0,退出自助查询系统。
#以下是运行代码：
def query_balance():
    # 模拟查询余额，这里返回一个固定的值
    balance = 100.0
    print(f"当前余额：{balance} 元")

def query_remainder():
    # 模拟查询剩余流量和通话时间，这里返回固定的值
    traffic = 10.0
    minutes = 500
    print(f"当前剩余流量：{traffic} G")
    print(f"当前剩余通话时间：{minutes} 分钟")

def main_menu():
    print("自助查询系统")
    print("1. 查询余额")
    print("2. 查询剩余流量和通话时间")
    print("3. 退出")
    choice = input("请选择一个操作（1/2/3）: ")
    return choice

def main():
    while True:
        action = main_menu()
        if action == '1':
            query_balance()
        elif action == '2':
            query_remainder()
        elif action == '3':
            print("退出自助查询系统。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()

"""

"""
实战三:
使用嵌套循环输出九九乘法表
需求:使用嵌套循环输出九九乘法表，内层循环与外层循环的关系，输出的
数据的个数与行数相同，即第一行输出一个，1*1=1，第二行输出两个
1*2=2 2*2=4 依次类推。
#以下是运行代码：
for i in range(1, 10):
    for j in range(1, i+1):
        product = i * j
        print(f"{i} * {j} = {product}")
    print()  # 输出一个空行，以便阅读
"""