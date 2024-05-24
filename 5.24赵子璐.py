#for _ in range(10):
    #print('hello',end=' ')


#x=y=z=1
#x=y=z
#def test_return():
#    return 4


#x = test_return()
#print(x)
#print(y)


#def test_return():
   # return 1,2


#x,y = test_return()
#print(x)
#print(y)


#def test_return() -> str:
#   return '你好世界'


#s = "你好，世界"
#byte_s = s.encode('utf-8')
#print(len(byte_s))  # 输出可能会是 15 或类似的数字，具体取决于编码后的字节数


#def my_function(*args):
#    for arg in args:
#        print(arg)


#my_function(1, 2, 3, 4)  # 输出: 1 2 3 4


#def func(*args):
#    the_max = args[0]
#    the_min = args[0]
#    for i in args:
#        if i > the_max:
#            the_max = i
#        elif i < the_min:
#            the_min = i
#    return {'max':the_max,'min':the_min}


#res = func(7,-20,3,40,-5)
#print(res)


def test_func(compute):
    result = compute(3,4)
    print(result)


def compute(x,y):
    return x + y


test_func(compute)


def test_func(compute):
    result = compute(3, 4)
    print(result)


def compute(x, y):
    return x * y


test_func(compute)


def test_func(compute):
    result = compute(3, 4)
    print(result)


def compute(x, y):
    return x - y


test_func(compute)