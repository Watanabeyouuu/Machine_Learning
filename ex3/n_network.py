"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: n_network.py
@date: 2020/11/16 4:16 下午

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
import matplotlib
from scipy.io import loadmat
from sklearn.metrics import classification_report  # 这个包是评价报告


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


data = loadmat('data/ex3data1.mat')
weight = loadmat("/home/kesci/input/andrew_ml_ex33507/ex3weights.mat")
rows = data['X'].shape[0]
params = data['X'].shape[1]

all_theta = np.zeros((10, params + 1))

X = np.insert(data['X'], 0, values=np.ones(rows), axis=1)

theta = np.zeros(params + 1)

y_0 = np.array([1 if label == 0 else 0 for label in data['y']])
y_0 = np.reshape(y_0, (rows, 1))

theta1, theta2 = weight['Theta1'], weight['Theta2']
print(theta1.shape, theta2.shape)

# 插入常数项
X2 = np.mat(np.insert(data['X'], 0, values=np.ones(X.shape[0]), axis=1))
y2 = np.mat(data['y'])
a1 = X2
z2 = a1 * theta1.T
a2 = sigmoid(z2)
a2 = np.insert(a2, 0, values=np.ones(a2.shape[0]), axis=1)
z3 = a2 * theta2.T
a3 = sigmoid(z3)
y_pred2 = np.argmax(a3, axis=1) + 1
print(classification_report(y2, y_pred))
