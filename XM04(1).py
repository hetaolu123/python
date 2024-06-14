# 课件四全部内容
# （四）列表_元组_字典_集合
"""
s = "helloworld"
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print('\n'+'-'*40)
for i in range(-10,0):
print(i,s[i],end='\t')
"""
"""
s = "helloworld"
s1 = s[0:5:2]
print(s1)
# 省略开始位置
print(s[:5:1])
#省略结束位置
print(s[0:7:1])
# 省略步长
print(s[0:6:])
# 省略开始位置、结束位置、步长
print(s[::])
"""

"""
#步长为负数，表示从后向前提取字符
s = "helloworld"
print(s[::-1])
print(s[-1:-11:-1])
print('-' * 40)
# 从0开始，向后方逆序步长为1输出，因为0左侧没有数值，所以为空
print(s[0:10:-1])
print('-'* 40)
print(s[4:-11:-1])
"""

"""
s = "helloworld"
print("e在s中存在吗?",'e' in s)
print("v在s中存在吗?",'v' in s)
print("e在s中不存在吗?",'e' not in s)
print("v在s中不存在吗?",'v' not in s)
# 内置函数的使用
print('len():', len(s))
print('max():', max(s))
print('min():', min(s))
print('s.index(o):',s.index('o'))
# print('s.index(v):',s.index('v'))#元素不存在时，报错如下:ValueError:substring not found
print('s.count(l):',s.count('l'))
"""

"""
#直接使用[]创建列表
lst=['hello','world',98,100.5]
print(lst)
#可以使用内置的函数list()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2)) #从1开始到1日结束，步长为2，不包含10
print(lst2)
print(lst3)
"""

"""
#列表是序列中的一种。对序列的操作符，运算符，函数均可以使用
print(lst+lst2+lst3) #序列中的相加操作
print(lst*3) #序列的相乘操作
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o')) #统计o的个数
print(lst2.index('o'))
"""

"""
#列表的删除操作
lst4=[10,20,30]
print(lst4)
#删除列表
del lst4
print(lst4) # NameError: name 'lst4' is not defined. Did you mean: 'lst'?
"""

"""
lst=['hello','world','python','php'] 
#使用遍历循环for遍历列表元素
for item in lst:
    print(item)
#使用for循环,range()兩数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
"""

"""
#第三种遍历方式enumearte()函数
for index,item in enumerate(lst):
    print(index,item)  #index是序号，不是索引
# 手动修改序号的起始值
for index,item in enumerate(lst,start=1): 
    print(index item)
    
for index,item in enumerate(lst,1):   #省略start不写，直接写起始值
    print(index,item)
"""

"""
lst=['hello','world','python']
print('原列表:',lst,id(lst))
#增加元素的操作
lst.append('sql')
print('增加元素之后:'lst,id(lst))
"""

"""
#使用insert(index,x)在指定的index位置上插入元素x
lst.insert(_index:1,_object: 100)
print(lst)
#列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表:',lst,id(lst))
"""

"""
#使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

#清除列表中所有的元素clear()
#lst.clear()
# print(lst,id(lst))

#列表的反向
lst.reverse() #不会产生新的列表，在原列表的基础上进行的
print(lst)
"""

"""
#列表的特贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改操作
# 根据索引进行修改元素
lst[1]='mysql'
print(lst)
"""

"""
lst=[4,56,3,78,40,56,89]
print('原列表:',lst)

#排序，默认是升序
lst.sort() #排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序:' lst)

#排序，降序
lst.sort(reverse=True)
print('降序:',lst)
"""

"""
lst2=['banana','apple','Cat','Orange']
print('原列表:',lst2)
#升序排序，先排大写、再排小写
lst2.sort()
print('升序:',lst2)
# 降序，先排小写，后排大写
lst2.sort(reverse=True)
print('降序:',lst2)
#忽略大小写进行比较
lst2.sort(key=str.lower)
print(lst2)
"""

"""
lst=[4,56,3,78,40,56,89]
print('原列表:',lst)
# 排序
asc_lst=sorted(lst)
print('升序:',asc_lst)
print('原列表:',lst)
#降序
desc_lst=sorted(lst,reverse=True)
print('降序:',desc_lst)
print('原列表:',lst)
"""

"""
lst2=['banana','apple','Cat','0range']
print('原列表:'lst2)
# 忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表:',lst2)
print('排序后的列表:,new_lst2)
"""

"""
import random
lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)
lst=[random.randint(a:1,b:100) for _ in range(10)]
print(lst)
#从列表中选择符合条件的元素组成新的列表
lst=[i for i in range(10) if i%2==0]
print(lst)
"""

"""
#创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,39]
]
print(lst)

#遍历二维列表使用双层for循环
for rowin lst: # 行
    for item in row:  #列
        print(item,end='\t')
        print() # 换行
#列表生成式生成一个4行5列的二维列表
lst2=[ [j for j in range(5)]for i in range(4)]
print(lst2)
"""

"""
# 使用小括号创建元组
t=('hello',[10,20,30],'python','world')
print(t)
# 使用内置函数tuple()创建元组
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)
"""

"""
print('10在元组中是否存在:',(10 in t))
print('10在元组是不存在: ',(10 not in t))
print('最大值:',max(t))
print('最小值:',min(t))
print('len:'len(t))
print('t.index:',t.index(10))
print('t.count',t.count(10))
"""

"""
#如果元组中只有一个元素
t=(10)
print(t,type(t))
#如果元组中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))
"""

"""
#元组的删除
del t
print(t)
"""

"""
t=('python','hello','world')
#根据索引访问元组
print(t[0])
t2=t[0:3:2]  #元组支持切片操作
print(t2)
#元组的遍历
for item in t:
    print(item)
# for+range()+len()
for i in range(len(t)):
    print(i,t[i])
"""

"""
for item in t:
    print(item)
# for+range()+len()
for i in range(len(t)):
    print(i,t[i])
# 使用enumerate()
for index,item in enumerate(t):
    print(index,'---->' item)
    
for index,item in enumerate(t,start=11): #序号从11开始
    print(index,'---->' item)
"""

"""
#(1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)  #key相同时，value值进行了覆盖

#(2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj) #<zip object at 0x000001ECD5A24F00>
#print(list(zipobj))    #[(10,'cat'),(20,'dog'),(30,'pet'),(40,'z0o')]
d=dict(zipobj)
print(d)        #{10:'cat'，20:'dog'，30:'pet'，40:'zoo'}
"""

"""
"""

"""
#使用参数创建字典
d=dict(cat=10,dog=20)   # 左侧cat是key，右侧的是value
print(d)

t=(10,20,30)
print({t:10})   #t是key,10是value，元组是可以作为字典中的key

#lst=[10,20,30]
# print({lst:10})  #TypeError: unhashable type: 'list

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
#字典的删除
del d
#print(d)
"""

"""
d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)
#向宇典中添加元素
d[1004]='张丽丽'  #直接使用赋值运算符向字典中添加元素
print(d)
#获取字典中所有的key
keys=d.keys()
print(keys) #dict_keys([1001，1002，1003，1004])
print(list(keys))
print(tuple(keys))

#获取字典中所有的value
values=d.values()
print(values)# dict_values(['李梅'，'王华'，'张峰'，'张丽丽'])
print(list(values))
print(tuple(valves))
"""

"""
#如果将字典中的数据转成key-value的形式,以元组的方式进行展现
1st=list(d.items())
print(lst)

d=dict(lst)
print(d)

# 使用pop丽数
print(d.pop(1001))
print(d)

print(d.pop(1008，"不存在'))

# 随机删除
print(d.popitem())
print(d)
#清空字典中所有的元素
d.clear()
print(d)
#Python中一切皆对象，每个对象部有一个布尔值
print(bool(d))  #空字典的布尔值为False
"""

"""
1mport random
d={item :random.randint( a:1,b:100)for item in range(4)}
print(d)

#创建两个列表
lst=[1001,1002,1003]
lst2=['陈梅梅'，'王一一''李丽丽']
d={key:value for key,value in zip(lst,lst2)}
print(d)
"""