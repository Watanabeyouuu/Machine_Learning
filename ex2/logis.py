"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: logis.py
@date: 2020/11/12 3:05 下午

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
import scipy.optimize as opt

path = 'data/ex2data1.txt'
data = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(data.head())


# 实现sigmoid函数
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# 实现代价函数
def cost(theta, X, y):
    theta = np.mat(theta)
    X = np.mat(X)
    y = np.mat(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))


# 加一列常数列
data.insert(0, 'Ones', 1)

# 初始化X，y，θ
cols = data.shape[1]
X = data.iloc[:, 0:cols - 1]
y = data.iloc[:, cols - 1:cols]
theta = np.zeros(3)

# 转换X，y的类型
X = np.array(X.values)
y = np.array(y.values)

# 检查矩阵的维度
print(X.shape, theta.shape, y.shape)


# 实现梯度计算的函数（并没有更新θ）
def gradient(theta, X, y):
    theta = np.mat(theta)
    X = np.mat(X)
    y = np.mat(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        term = np.multiply(error, X[:, i])
        grad[i] = np.sum(term) / len(X)

    return grad


# 用初始θ计算代价
print(cost(theta, X, y))
result = opt.fmin_tnc(func=cost, x0=theta, fprime=gradient, args=(X, y))
print(result[0])
print(cost(result[0], X, y))

positive = data[data['Admitted'].isin([0])]
negative = data[data['Admitted'].isin([1])]
plotting_x1 = np.linspace(30, 100, 100)
print(plotting_x1)
plotting_h1 = (- result[0][0] - result[0][1] * plotting_x1) / result[0][2]

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(plotting_x1, plotting_h1, 'y', label='Prediction')
ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
plt.show()


# 实现hθ
def hfunc1(theta, X):
    return sigmoid(np.dot(theta.T, X))


print(hfunc1(result[0], [1, 45, 85]))


# 定义预测函数
def predict(theta, X):
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]


# 统计预测正确率
theta_min = np.mat(result[0])
predictions = predict(theta_min, X)
correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
accuracy = (sum(map(int, correct)) % len(correct))
print('accuracy = {0}%'.format(accuracy))
