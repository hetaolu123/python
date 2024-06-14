'''# 变量a，值为100
a = 100
# 变量b，值为50
b = 50
print(90)
# 输出的是变量的值 ，a的值是100print(a*b)# 输出a*b的运算结果，运算结果为5000
print(a)
print('北京欢迎你!')
print("北京欢迎你!")
print('北京欢迎你!')
print("""北京欢迎你!""")'''

'''输出多条语句'''
'''a = 100
b = 50
print(a, b, '要么出众，要么出局！')'''


'''ASCII码'''
'''print(chr(98))
# 也输出了b 使用chrO将98转换成ASCII表中的字符print('C')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
# 中文编码的范围是[u4e00~u9fa5]'''
print(ord('北'))
print(ord('京'))
print(chr(21271), chr(20140))


fp = open('note.text', 'w')#打开文件w--》write
print('北京欢迎你',file=fp)#将“北京欢迎你”输出到文件中
fp.close()# 关闭文件


print('北京欢迎你'+'2023')


# Press the green button in the gutter to run the script.
def print_hi(param):
    pass


if __name__=='_main__':
    print_hi('PyCharm')
    # 单行注释
    # print('我的第一个Python程序!)
    # #print('我的第二个Python程序')
'''多行注释
fp = open('note.txt', 'w')
print('北京欢迎你',file=fp)
fp.close()'''
'''name = input('请输入您的姓名：')
print('我的姓名是：' + name)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


num = input("请输入您的幸运数字：")
print('您的幸运数字是' + num)
num = int(num)
print('您的幸运数字是', num)'''


'''print(1, 2, 3)
fp = open('test.txt', 'w')
print(1, 2, 3, 'sep=---', end='<+++>',file=fp)
fp.close()'''