import random
import time
import numpy as np

'''
# 直接用 NumPy 生成数据，避免 Python 循环
b = np.random.random(100000000)
a = b.tolist()  # 转为 Python 列表

# 测试 Python 内置 sum
t1 = time.time()
sum1 = sum(a)
t2 = time.time()

# 测试 NumPy sum
t3 = time.time()
sum2 = np.sum(b)
t4 = time.time()

print(f"Python sum: {t2 - t1:.4f}s")
print(f"NumPy sum:  {t4 - t3:.4f}s")
'''

"""
list1= [1,2,3,4]
oneArray=np.array(list1)
print("oneArray = ", oneArray)
print(type(oneArray))

#创建数组的多种形式
# 1.直接传入列表的方式
t1=np.array([1,2,3])
print("t1 = ", t1)
print(type(t1))
'''
[1 2 3]
<class 'numpy.ndarray'>
'''
# 2.传入range生成序列
t2=np.array(range(10))
print("t2 = ", t2)
print(type(t2))
'''
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
'''
# 3.使用numpy自带的np.arange()生成数组
t3=np.arange(0,11,2)
print("t3 = ", t3)
print(type(t3))
'''
[0 2 4 6 8]
<class 'numpy.ndarray'>
'''
"""

'''
list2= [[1,2],[3,4],[5,6]]
twoArray=np.array(list2)
print(twoArray)
'''

'''
list2= [[1,2],[3,4],[5,6]]
twoArray=np.array(list2)
#获取数组的维度(注意： 与函数的参数很像)
print(twoArray.ndim)
#形状（行，列）
print(twoArray.shape)
#有多少个元素
print(twoArray.size)
'''

'''
four=np.array([[1,2,3],[4,5,6]])
#修改的是原有的
four.shape= (3,2)
print(four)
#返回一个新的数组
four=four.reshape(3,2)
print(four)
#将多维变成一维数组
five=four.reshape((6,),order='F')
#默认情况下‘C’以行为主的顺序展开，‘F’（Fortran风格）意味着以列的顺序展开
six=four.flatten(order='F')
print(five)
print(six)
#拓展：数组的形状
t=np.arange(24)
print(t)
print(t.shape)
#转换成二维
t1=t.reshape((4,6))
print(t1)
print(t1.shape)
'''

'''
#将数组转成list
a=np.array([9,12,88,14,25])
list_a=a.tolist()
print(list_a)
print(type(list_a))
'''


'''
import random
#返回数组中每个元素的字节单位长度, dtype设置数据类型
f=np.array([1,2,3,4,5],dtype=np.int16)
print(f.itemsize)# 1 np.int8(一个字节)
#获取数据类型
print(f.dtype)
#调整数据类型
f1=f.astype(np.int64)
print(f1.dtype)
#拓展随机生成小数
#使用python语法, 保留两位
print(round(random.random(),2))
arr=np.array([random.random() for i in range(10)])  
#取小数点后两位
print(np.round(arr,2))
'''

"""
t1 = np.arange(24).reshape((4,6))
t2 = np.arange(18).reshape((3,6))
print(t1)
print(t2)
print(t1-t2)
'''
ValueError: operands could not be broadcast together with shapes (4,6) (3,6)
'''
"""

'''
a = np.arange(10)
print(a[2],a)
print(a[2:])
'''


# ========== NumPy 二维数组的索引和切片 ==========
# 索引格式: t1[行, 列]  ':'表示全部, 'a:b'表示切片(左闭右开), [a,b,c]表示不连续选取

# 创建一个4行6列的二维数组(0~23)
t1 = np.arange(24).reshape(4,6)
print("t1 = ", t1)
print('*'*20)

# --- 取行操作 ---
print("t1[1] = ", t1[1])      # 取第2行(索引从0开始), 等价于 t1[1,:]
print('*'*20)

print("t1[1:] = ", t1[1:])     # 取第2行到最后一行(连续多行)
print('*'*20)

print("t1[1:3,:] = ", t1[1:3,:])  # 取第2~3行(左闭右开, 不包含索引3)
print('*'*20)

print("t1[[0,2,3]] = ", t1[[0,2,3]])    # 取第1、3、4行(不连续多行, 用列表指定行索引)
print('*'*20)

print("t1[[0,2,3],:] = ", t1[[0,2,3],:])  # 同上, 加 ':' 表示取这些行的所有列
print('*'*20)

# --- 取列操作 ---
print("t1[:,1] = ", t1[:,1])        # 取第2列(':' 表示所有行, 1 表示第2列)
print('*'*20)

print("t1[:,1:] = ", t1[:,1:])       # 取第2列到最后一列(连续多列)
print('*'*20)

print("t1[:,[0,2,3]] = ", t1[:,[0,2,3]])  # 取第1、3、4列(不连续多列)
print('*'*20)

# --- 取单个值 ---
print("t1[2,3] = ", t1[2,3])        # 取第3行第4列的值, 即15
print('*'*20)
