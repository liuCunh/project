import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

x = np.linspace(-6, 5, 500)  # 设置x轴取值范围
y = x ** 2 + 3
plt.plot(x, y, color='r')
plt.title("curve")
x1 = np.linspace(-6, 5, 500)
y1 = 3*x+2
plt.plot(x1, y1)
plt.show()


plt.subplot(221)
x = [1, 2, 3, 4]
y = [4, 7, 3, 9]
plt.plot(x, y)
plt.subplot(222)
plt.bar(x, y, color='r')  # 条形图
plt.subplot(223)
plt.scatter(x, y, color='b')  # 散点图
plt.subplot(224)
plt.barh(x, y, color='y')  # 量图
plt.show()


x = range(1000)
y = [sqrt(_) for _ in x]
plt.plot(x, y, color='blue', lw=5)
plt.fill_between(x, y, color="lightblue")  # 函数与x轴之间的填充
plt.show()

x = np.arange(1, 4*np.pi, 0.01)
y = np.cos(x)
z = np.sin(x)
plt.figure()
plt.subplot(121)
plt.title("余弦")
plt.plot(x, y, color='r')
plt.subplot(122)
plt.title("正弦")
plt.plot(x, z, color='c')
plt.show()