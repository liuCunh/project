import numpy as np
import pandas as pd

df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
df['col4'] = [7, 8]  # 增加一个字段
df = df.reindex(['a', 'b', 'c'])  # 增加记录,必须接收返回值
df = df.drop('c')  # 删除记录，必须要接收
df = df.drop(['col1', 'col2'], axis=1)  # 删除多条, 1表示字段， 0表示记录
df = df.reindex(['a', 'b', 'c'])
d = {"col3": 4, "col4": 3}
df = df.append(d, ignore_index=True)  # 增加数据列
df.loc[2, "col3"] = 1  # 修改数据

df = pd.DataFrame({"one": [1, 4, 2, 7], "two": [6, 2, 8, 3]})
print(df)
df = df.sort_values(by='one')  # 通过one关键字进行排序

print(df.idxmin(axis=0))  # 字段中返回最小值
print(df.idxmin(axis=1))  # 记录中返回最小值的index
