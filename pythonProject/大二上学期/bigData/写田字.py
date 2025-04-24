import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False  # 设置负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字
x, y = [1, 1, 3, 3, 1], [1, 3, 3, 1, 1]
plt.plot(x, y)
x1, y1 = [2, 2], [1, 3]
plt.plot(x1, y1)
x2, y2 = [1, 3], [2, 2]
plt.plot(x2, y2)
plt.title("刘春")
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
