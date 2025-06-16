import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# 1
# a
fertilizer = np.array([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])
potatoes = np.array([7.5, 10.2, 12.8, 14.5, 15.6, 16, 15.8, 15, 13.5, 11.2])
xSquared = fertilizer ** 2
xy = fertilizer * potatoes
xSquaredY = xSquared * potatoes
print(xSquared, xy, xSquaredY)

# b
polynomial_model = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('linear', LinearRegression())
])
polynomial_model.fit(fertilizer.reshape(-1, 1), potatoes)

# c
coefficients = polynomial_model.named_steps['linear'].coef_
intercept = polynomial_model.named_steps['linear'].intercept_
optimal_fert = -coefficients[1] / (2 * coefficients[2])
print(f"Optimal fertilizer amount: {optimal_fert}")

# d
print(f"Max yield: {polynomial_model.predict([[optimal_fert]])[0]:.2f} potatoes tons")

# 2
# a
fertilizer = np.array([100, 150, 200, 250, 300, 200, 200, 200, 200, 200, 200, 200, 200, 200])
irrigation = np.array([5, 5, 5, 5, 5, 3, 4, 6, 7, 5, 5, 5, 5, 5])
temperature = np.array([20, 20, 20, 20, 20, 20, 20, 20, 20, 15, 18, 22, 25, 28])
corn = np.array([2.5, 3.2, 3.8, 4.1, 3.9, 3.0, 3.5, 3.9, 3.7, 3.2, 3.6, 3.7, 3.5, 3.1])

x = np.column_stack((fertilizer, irrigation, temperature))
y = corn

poly = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
fert_grid = np.linspace(100, 300, 30)
irri_grid = np.linspace(3, 7, 30)
temp_grid = np.linspace(15, 28, 30)
fert_mesh, irri_mesh, temp_mesh = np.meshgrid(fert_grid, irri_grid, temp_grid)

x_grid = np.column_stack((fert_mesh.ravel(), irri_mesh.ravel(), temp_mesh.ravel()))
x_grid_poly = poly.transform(x_grid)
corn_pred = model.predict(x_grid_poly).reshape(fert_mesh.shape)

max_corn = np.max(corn_pred)
max_idx = np.unravel_index(np.argmax(corn_pred), corn_pred.shape)
optimal_fert = fert_mesh[max_idx]
optimal_irri = irri_mesh[max_idx]
optimal_temp = temp_mesh[max_idx]

print(f"Model polynomial coefficients: {model.coef_}")
print(f"Optimal fertilizer amount: {optimal_fert:.2f} liters ")
print(f"Optimal irrigation amount: {optimal_irri:.2f} water")
print(f"Optimal temperature amount: {optimal_temp:.2f} degrees")
print(f"Maximum predicted corn amount: {max_corn:.2f} kg")

# 3
# a
# You need to scale features in models inorder to balance changes across features, for example
# If a certain feature is 1-5 and another feature is 10000-20000 there are big differences between them
# so scaling in used to mitigate the differences.

# b
X1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
X2 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

xsStacked = np.column_stack((X1, X2))

# c
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled = scaler.fit_transform(xsStacked)
print(scaled)
# d
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled = scaler.fit_transform(xsStacked)
print(scaled)

# e
# MinMax scaling is transforming the values from 0 to 1, like a percentile
# Standardization is transforming the values to stds count, usually from -3 to 3

# 4
import matplotlib.pyplot as plt
# a
Exercise = [0.0, 0.53, 1.05, 1.58, 2.11, 2.63, 3.16, 3.68, 4.21, 4.74,
            5.26, 5.79, 6.32, 6.84, 7.37, 7.89, 8.42, 8.95, 9.47, 10.0]
Calories = [7.99, 9.17, 11.91, 12.89, 9.70, 11.32, 15.49, 17.53, 20.27, 20.92,
            24.76, 24.80, 26.36, 26.21, 29.41, 33.71, 31.72, 36.96, 32.63, 35.60]

anxiety_level = [-4.0, -3.58, -3.16, -2.74, -2.32, -1.89, -1.47, -1.05, -0.63, -0.21,
                 0.21, 0.63, 1.05, 1.47, 1.89, 2.32, 2.74, 3.16, 3.58, 4.0]
self_esteem = [41.02, 43.27, 39.14, 25.96, 23.08, 16.41, 14.31, 12.26, 1.91, 5.65,
               3.80, -5.23, -10.89, -2.85, -3.41, -3.34, -0.75, 13.14, 11.03, 17.77]

plt.scatter(Exercise, Calories)
plt.title("Exercise vs Calories")
plt.show()

plt.scatter(anxiety_level, self_esteem)
plt.title("anxiety vs self esteem")
plt.show()

#b
from sklearn.metrics import r2_score
model = LinearRegression()
Exercise = np.array(Exercise).reshape(-1, 1)
Calories = np.array(Calories)
model.fit(Exercise, Calories)
calories_pred = model.predict(Exercise)
r2 = r2_score(Calories, calories_pred)
print(r2)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(Calories, calories_pred)
print(mse)

plt.scatter(Exercise, calories_pred)
plt.xlabel("Exercise")
plt.ylabel("Calories")
plt.plot(Exercise, calories_pred, c="purple")
plt.show()

# The model fits

# c
linear_model = LinearRegression()
polynomial_model = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('linear', LinearRegression())
])
anxiety_level = np.array(anxiety_level).reshape(-1, 1)
self_esteem = np.array(self_esteem)
linear_model.fit(anxiety_level, self_esteem)
polynomial_model.fit(anxiety_level, self_esteem)
lin_esteem_pred = linear_model.predict(anxiety_level)
poly_esteem_pred = polynomial_model.predict(anxiety_level)
r2lin = r2_score(self_esteem, lin_esteem_pred)
r2poly = r2_score(self_esteem, poly_esteem_pred)
mseLin = mean_squared_error(self_esteem, lin_esteem_pred)
msePoly = mean_squared_error(self_esteem, poly_esteem_pred)
print(f"r2lin:{r2lin}, r2poly:{r2poly}, mseLin:{mseLin}, msePoly:{msePoly}")

plt.scatter(anxiety_level, lin_esteem_pred)
plt.title("Linear")
plt.xlabel("Anxiety")
plt.ylabel("Self esteem")
plt.show()

plt.scatter(anxiety_level, poly_esteem_pred)
plt.title("Linear")
plt.xlabel("Anxiety")
plt.ylabel("Self esteem")
plt.show()

# The polynomial model is more suitable here