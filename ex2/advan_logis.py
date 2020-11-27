"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: advan_logis.py
@date: 2020/11/12 4:12 下午

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

path = 'data/ex2data2.txt'
data_init = pd.read_csv(path, header=None, names=['Test 1', 'Test 2', 'Accepted'])
print(data_init.head())

positive2 = data_init[data_init['Accepted'] == 1]
negative2 = data_init[data_init['Accepted'] == 0]
fig, ax = plt.subplots(figsize=(12, 8))
ax.scatter(positive2['Test 1'], positive2['Test 2'], s=50, c='b', marker='o', label='Accepted')
ax.scatter(negative2['Test 1'], negative2['Test 2'], s=50, c='r', marker='x', label='Rejected')
ax.set_xlabel('Test 1 Score')
ax.set_ylabel('Test 2 Score')
plt.show()

degree = 6
data2 = data_init
x1 = data2['Test 1']
x2 = data2['Test 2']
data2.insert(3, 'Ones', 1)

for i in range(1, degree + 1):
    for j in range(0, i + 1):
        data2['F' + str(i - j) + str(j)] = np.power(x1, i - j) * np.power(x2, j)
# 此处原答案错误较多，已经更正
print(data2)
data2.drop('Test 1', axis=1, inplace=True)
data2.drop('Test 2', axis=1, inplace=True)

data2.head()
