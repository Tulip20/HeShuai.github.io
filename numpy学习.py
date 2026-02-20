import random
import time
import numpy as np

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