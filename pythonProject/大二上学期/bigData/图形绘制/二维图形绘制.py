import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
# x = np.arange(10)
# y = np.random.randint(0, 100, 10)
# lables = [f"{i}班" for i in range(1, 11)]
# plt.bar(x, y, color='r', tick_label=lables)
# plt.title("班级平均成绩-刘春")
# plt.legend(["平均成绩"])  # 图例说明
# plt.xlabel("x轴")
# plt.ylabel("y轴")
# plt.show()

# 实训一
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.title("学生学习能力对比-刘春")
# x = np.arange(1, 11)
# plt.plot(x, x*1.2)
# plt.plot(x, x*2)
# plt.plot(x, x*3)
# plt.plot(x, x*4)
# plt.legend(["黄亚兰", "周兰", "胡飞", "赵云"])
# plt.show()


# # 实训二
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
GDP = [28000, 30133, 18590, 19500]
plt.bar(range(4), GDP, align="center", color="lightblue", alpha=1)
plt.ylabel("GDP")
plt.title("2021年四个直辖市GDP对比-刘春")
plt.xticks(range(4), ['北京市', '上海市', '天津市', '重庆市'])
plt.ylim([5000, 35000])
plt.show()
