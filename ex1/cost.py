"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: cost.py
@date: 2020/10/24 3:48 下午

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳ ┃
            ┃     ┻   ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━━━┓┓┏━━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path = 'data/ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
data.head()

data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
plt.show()


def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


data.insert(0, 'Ones', 1)
cols = data.shape[1]

X = data.iloc[:, :-1]  # X是data里的除最后列
y = data.iloc[:, cols - 1:cols]  # y是data最后一列
print(X.head())
# aa = computeCost(data, data[:, :-1], theta)
# print(aa)
X = np.mat(X.values)
y = np.mat(y.values)
theta = np.mat(np.array([0, 0]))
print(X.shape, theta.shape, y.shape)
cost = computeCost(X, y, theta)
print(cost)


def gradientDescent(X, y, theta, alpha, iters):  # 这个部分实现了Ѳ的更新
    temp = np.mat(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


alpha = 0.01
iters = 1500
g, costG = gradientDescent(X, y, theta, alpha, iters)
print(g)

predict1 = [1, 3.5] * g.T
print("predict1:", predict1)
predict2 = [1, 7] * g.T
print("predict2:", predict2)
# 预测35000和70000城市规模的小吃摊利润
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()
