# # Our data
# hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Study hours
# exam_scores = np.array([60, 65, 70, 75, 80, 85, 90, 92, 95])  # Exam scores
#
# # Create regression model
# model = LinearRegression()
# model.fit(hours_studied, exam_scores)
#
# # Print results
# print(f"Slope (m): {model.coef_[0]:.2f}")
# print(f"Intercept (b): {model.intercept_:.2f}")
#
# # Calculate equation
# equation = f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"
# print(f"Line equation: {equation}")
#
# # Predict hours needed to get score of 100
# score_to_predict = 100
# hours_needed = (score_to_predict - model.intercept_) / model.coef_[0]
# print(f"To get a score of 100, approximately {hours_needed:.2f} hours of study are needed")
#
# # Create the graph
# plt.figure(figsize=(10, 6))
# plt.scatter(hours_studied, exam_scores, color='blue', label='Data points')
# plt.plot(hours_studied, model.predict(hours_studied), color='red', label='Regression line')
#
# # Add prediction point
# plt.scatter([[hours_needed]], [100], color='green', s=100, label='Our prediction')
#
# # Add labels in English
# plt.title('Linear Regression - Study Hours vs. Exam Score')
# plt.xlabel('Study Hours')
# plt.ylabel('Exam Score')
# plt.grid(True)
# plt.legend()
#
# # Display equation on the graph
# plt.text(1, 95, equation, fontsize=12)
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy
import seaborn as sns
import pandas as pd
# 1

ads = np.array([10,15,20,25,30,35,40,45,50]).reshape(-1, 1)
sales = np.array([25,30,40,45,50,60,65,70,80])

model = LinearRegression()
model.fit(ads, sales)
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

#a
equation = f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"
print(f"Line equation: {equation}")

#d
ads = ads.reshape(-1)
p = np.polyfit(ads, sales, 1)
print(p)

# 2
hours = np.array([2,3,4,5,6]).reshape(-1,1)
income = np.array([50,70,90,100,110])

model = LinearRegression()
model.fit(hours, income)

#a
m = model.coef_[0]
b = model.intercept_


plt.figure(figsize=(10, 6))
plt.scatter(hours, income, color='blue', label='Data points')

#bonus
xrange = np.linspace(6,20).reshape(-1,1)
plt.plot(xrange, model.predict(xrange), color='red', label='Regression line')
plt.title('Linear Regression - Hours vs. Income')
plt.xlabel('Hours')
plt.ylabel('Income')
plt.grid(True)
plt.legend()

eightHours = 8
eightHoursPred = m*8 + b
print(f"Expected Income after {eightHours} hours = {eightHoursPred}")

hundredFifty = 150
hundredFiftyPred = (150-b)/m
print(f"Expected hours for {hundredFifty}K dollar = {hundredFiftyPred}")

#bonus
df = pd.DataFrame({'hours': hours.reshape(-1), 'income': income})
sns.regplot(data = df, x = df.hours, y = df.income)

plt.show()