import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
plt.rcParams['axes.unicode_minus'] = False  # 设置负号
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_values = [1.2, 2.2, 1.3, 1.6, 25, 2.2, 3.1, 3.6, 2.8, 1.9]
plt.scatter(x_values, y_values, s=100)  # s 点的大小
plt.title("刘春", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Scatter of Value", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)  # 刻度标记大小
plt.show()
