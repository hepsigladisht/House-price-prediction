# -*- coding: utf-8 -*-
"""house price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RoC38MYxS5Qvg2PJyE2kXOqSa4l7HbxQ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv("house_data.csv")
print(data.head())
X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, r2_score
print("MAE:", mean_absolute_error(y_test, predictions))
print("R² Score:", r2_score(y_test, predictions))

plt.scatter(y_test, predictions)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red')  # regression reference line
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()