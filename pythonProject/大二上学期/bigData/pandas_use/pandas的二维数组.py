import numpy as np
import pandas as pd

data = {"name": ["owen", "tome"], "year": ["1990", "1998"]}
frame = pd.DataFrame(data, columns=['name', 'year'], index=['one', 'two'])  # columns规定字段头， index规定记录头
print(frame)
res = 'tome' in frame.index  # 查看键
print(res)
res1 = "owen" in frame.values  # 查看值
print(res1)
print(frame.shape)  # 查看数组大小
print(frame.values)  # 查看数组中的值

data_arr = [['tom', 25, '男'], ['Jerry', 23, '男']]
df = pd.DataFrame(data_arr, columns=['name', 'age', 'gender'])
print(df)
data = [np.array(('tom', 'ben', 'messi')), np.array((23, 32, 18)), np.array(('male', 'female', 'femile'))]
print(data)
pd_np = pd.DataFrame(data, index=['name', 'age', 'gender'])  # 横向数组
print(pd_np)
print("tom" in pd_np.values)
# for i in pd_np.values:
#     print(i)

