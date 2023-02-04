import pandas as pd
import matplotlib.pyplot as plt

# 1.
data = pd.read_csv('5.csv')
print(data)
# 2.
print(data.head())
# 3.
print(data.describe())
# 4.
print(data.shape)
# 5.
print(data.dtypes)
# 6.
iris = pd.read_csv("iris.csv")
print(iris)
# 7.
print(iris.head())
# 8.
iris.plot(y="Sepal.Length", x="Sepal.Width", kind="scatter")

# 9.
iris.plot(x="Petal.Width", y="Petal.Length", kind="scatter")
plt.show()
