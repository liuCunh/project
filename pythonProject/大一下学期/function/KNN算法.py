from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 导入鸢尾花数据表
iris = load_iris()
# 鸢尾花花瓣长度数据
x = iris.data
# 构建模型
model = KMeans(n_clusters=3)
# 训练
model.fit(x)
# 预测
y = model.predict(x)
print('预测结果：', y)
# 画图
plt.scatter(x[:, 2], x[:, 3], c=y, s=50, cmap='rainbow')
plt.show()
