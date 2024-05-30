#def fun1(x, y):
#    print("这是函数一")
#    sum = x + y
#    return sum


#def fun2():
#   print("这是函数二")
#    sum = fun1(4, 7)
#    print(sum)
#fun2()


#def max(x, y):
#    return x if x > y else y


#def maxs(a, b, c, d):
#    res1 = max(a, b)
#    res2 = max(res1, c)
#    res3 = max(res2, d)
#    return res3


# print(maxs(5, 2, 586, 299))


# n的阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)# 递归函数


# eg:
num = 5
result = factorial(num)
print(f"The factorial of {num} is:{result}")