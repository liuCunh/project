import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
# 矩形中绘制小矩形
x, y = [1, 1, 8, 8, 1], [1, 5, 5, 1, 1]
plt.plot(x, y)
x1, y1 = [3, 3, 6, 6, 3], [2, 4, 4, 2, 2]
plt.plot(x1, y1)
plt.title("矩形")
plt.show()

# # 矩形
# x, y = [1, 1, 10, 10, 1], [1, 2, 2, 1, 1]
# plt.plot(x, y)
# plt.title("矩形")
# plt.show()

# # 三角形
# x, y = [2, 3, 4, 2], [2, 7, 2, 2]
# plt.plot(x, y)
# plt.title("triangle")
# plt.show()

# # 矩形中绘制小矩形
# x, y = [1, 1, 8, 8, 1], [1, 5, 5, 1, 1]
# plt.plot(x, y)
# x1, y1 = [3, 3, 6, 6, 3], [2, 4, 4, 2, 2]
# plt.plot(x1, y1)
# plt.title("矩形")
# plt.show()


# # 曲线
# plt.rcParams['axes.unicode_minus'] = False  # 设置负号
# x = np.linspace(0.05, 10, 1000)  # x轴信息
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, ls="-", lw=2, color="c", label="plot figure")
# plt.plot(x, z, ls=":", lw=3, color="r")
# plt.xlabel("x轴")
# plt.ylabel("y轴")
# plt.title("曲线")
# plt.text(3.10, 0.09, "y=sin(x)", color="b")
# plt.legend()
# plt.show()
