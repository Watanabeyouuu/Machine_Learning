"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: line.py
@date: 2020/11/26 9:22 下午
"""
print(__doc__)

# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

sales = pd.read_csv("ex1.csv")
sales = pd.DataFrame(sales)
sales = sales.values
# Load the diabetes dataset
diabetes_X = sales[:, 2:]
diabetes_y = sales[:, 1:2].reshape(10, )
# diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
print(diabetes_X, diabetes_y)
# print(diabetes_X.shape, diabetes_y.shape)
# Use only one feature
# diabetes_X = diabetes_X[:, np.newaxis, 2]
print(diabetes_X)
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-2]
diabetes_X_test = diabetes_X[-2:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-2]
diabetes_y_test = diabetes_y[-2:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
# plt.scatter(diabetes_X_train, diabetes_y_train, color='black')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
