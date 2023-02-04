import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("3.csv", header=0)  # 读取CSV文件，header：从第几行开始读取
print(df, "\n")
# print(df.dtypes)  # 显示字段数据类型
# print(df.head())  # 显示数据集中前5数据
# print(df.info())
# print(df.describe())  # 对数据进行运算
# print(df.shape)  # 形状

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
# df = pd.read_csv('iris.csv')
# print(df.head())
# print(df.describe())  # 显示数据集特征
# df.plot(x="Petal.Length", y="Petal.Width", kind='scatter')  # kind说明图形类型
# plt.title("分析数据集特征")
# plt.show()


s = pd.DataFrame(np.random.randn(100), columns=['value'])
print(s.head())
print(s.describe())
plt.scatter(s.index, s.values)  # 散点图
plt.show()
