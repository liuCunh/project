import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
# x, y = [1, 2, 3, 4], [5, 6, 7, 8]
#
# # 设置标题
# plt.title("性别")
# # 绘制直线图
# plt.plot(x, y, color="r")
# # 将图形展示
#
# # 点图
# plt.scatter(x, [12, 23, 12, 15], color="y")
#
# # 设置坐标轴
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

# x = [1, 2, 3, 4, 1]
# y = [2, 4, 4, 2, 2]
# plt.plot(x, y)
# x1 = [2, 2.5, 3, 2]
# y1 = [2.25, 3, 2.25, 2.25]
# plt.plot(x1, y1)
# plt.title("直线")
# plt.show()

plt.rcParams['axes.unicode_minus'] = False  # 设置负号
x = np.linspace(0.05, 10, 1000)  # x轴信息
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, ls="-", lw=2, color="c", label="plot figure")
plt.plot(x, z, ls=":", lw=3, color="r")
plt.xlabel("x轴")
plt.ylabel("y轴")
plt.title("曲线")
plt.text(3.10, 0.09, "y=sin(x)", color="b")
plt.legend()
plt.show()
