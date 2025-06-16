import numpy as np
import matplotlib.pyplot as plt

# 1
# a
ads = np.array([10,15,20,25,30,35,40,45,50])
sales = np.array([25,30,40,45,50,60,65,70,80])

alpha = 0.001
iters = 100000
m = 0
b = 0
n = len(ads)

cost_hist = []

for i in range(iters):
    sales_pred = m * ads + b

    cost = (1/(2*n)) * np.sum((sales_pred - sales)**2)
    cost_hist.append(cost)

    m_gradient = (1/n) * np.sum(ads * (sales_pred - sales))
    b_gradient = (1/n) * np.sum(sales_pred - sales)

    m = m - alpha * m_gradient
    b = b - alpha * b_gradient

    if i % 10000 == 0:
        print(f"Iteration {i}: m = {m:.4f}, b = {b:.4f}, cost = {cost:.4f}")

#b

ads60 = 60
income_expected = m*ads60 + b
print(f"Expected income after {ads60} ads invest = {income_expected}")

#c
income100 = 100
ads_needed = (100 - b)/m
print(f"Expected ads for {income100}, = {ads_needed}")

#d
alpha = 0.001
iters = 100000
m = 0
b = 0
n = len(ads)

cost_hist = []

for i in range(iters):
    sales_pred = m * ads + b

    cost = (1/(2*n)) * np.sum((sales_pred - sales)**2)
    cost_hist.append(cost)

    m_gradient = (1/n) * np.sum(ads * (sales_pred - sales))
    b_gradient = (1/n) * np.sum(sales_pred - sales)

    m = m - alpha * m_gradient
    b = b - alpha * b_gradient

    if i % 10000 == 0:
        print(f"Iteration {i}: m = {m:.4f}, b = {b:.4f}, cost = {cost:.4f}")

print("Original----------------------------------------------------------")

alpha = 0.0001
iters = 100000
m = 0
b = 0
n = len(ads)

cost_hist = []

for i in range(iters):
    sales_pred = m * ads + b

    cost = (1/(2*n)) * np.sum((sales_pred - sales)**2)
    cost_hist.append(cost)

    m_gradient = (1/n) * np.sum(ads * (sales_pred - sales))
    b_gradient = (1/n) * np.sum(sales_pred - sales)

    m = m - alpha * m_gradient
    b = b - alpha * b_gradient

    if i % 10000 == 0:
        print(f"Iteration {i}: m = {m:.4f}, b = {b:.4f}, cost = {cost:.4f}")
print("Slower----------------------------------------------------------")

alpha = 0.00001
iters = 100000
m = 0
b = 0
n = len(ads)

cost_hist = []

print("")

for i in range(iters):
    sales_pred = m * ads + b

    cost = (1/(2*n)) * np.sum((sales_pred - sales)**2)
    cost_hist.append(cost)

    m_gradient = (1/n) * np.sum(ads * (sales_pred - sales))
    b_gradient = (1/n) * np.sum(sales_pred - sales)

    m = m - alpha * m_gradient
    b = b - alpha * b_gradient

    if i % 10000 == 0:
        print(f"Iteration {i}: m = {m:.4f}, b = {b:.4f}, cost = {cost:.4f}")
print("Even Slower----------------------------------------------------------")

# 2 We'd rather solve using Gradient Descent in cases of polynomials and multiple variables.

# 3
# a
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

X = np.array([
    [2,15,40,0],
    [5,16,45,1],
    [3,16,40,0],
    [10,18,50,5],
    [7,17,45,3],
    [1,14,35,0],
    [8,16,45,4],
    [4,15,40,1],
    [6,15,42,2],
    [12,19,55,8]

])

y = np.array([15,25,18,45,35,12,38,22,30,60])

model = LinearRegression()
model.fit(X, y)

# a
print(f"Intercept (β₀): {model.intercept_:.2f}")
print(f"Coefficients (β₁, β₂, β₃, β₄): {model.coef_}")

# b
print(f"F(x) =  {model.coef_[0]}x₁ + {model.coef_[1]}x₂ + {model.coef_[2]}x₃ + {model.coef_[3]}x₄ + {model.intercept_}")

# c
y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

n = X.shape[0]
k = X.shape[1]
adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)
print(f"R² = {r2}")
print(f"Adjusted R² = {adjusted_r2}")

# d
worker = np.array([6,16,43,2])
expected_salary = model.intercept_
for i in zip(model.coef_, worker):
    expected_salary += i[0]*i[1]
print(f"The expected salary is {expected_salary}k")

# e
# The most important variables by descending order: Managing, Experience, Work hours, Education.

# Computational question
#a
predicted_salary = 2.5*10 + 1.2*16 + 0.8*42 + 5
print(f"The predicted salary is {predicted_salary}")

#b
print(f"The residual is {65 - predicted_salary}")
