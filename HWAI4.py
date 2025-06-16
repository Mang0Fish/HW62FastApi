import math
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1

y_true = np.array([
    10.5, 8.2, 7.3, 15.4, 12.0,
    9.8, 6.7, 11.2, 13.5, 9.0,
    8.1, 14.2, 10.0, 7.5, 12.8,
    9.3, 11.8, 8.9, 10.7, 13.1
])

# predicted values
y_pred = np.array([
    11.2, 7.8, 7.0, 16.1, 11.5,
    9.5, 7.2, 10.8, 14.0, 8.7,
    8.5, 13.9, 10.4, 7.8, 12.5,
    9.0, 12.3, 9.4, 11.1, 12.8
])

mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = math.sqrt(mse)

# 2
from sklearn.linear_model import LinearRegression
import joblib

# X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # reshape for sklearn
# y = np.array([2, 4, 5, 4, 5, 7, 8, 9, 11, 12])
#
# # Fit the model
# model = LinearRegression()
# model.fit(X, y)
# print("Model fitted")
# print(f"Coefficient: {model.coef_[0]:.4f}")
# print(f"Intercept: {model.intercept_:.4f}")
#
# new_data = np.array([5]).reshape(-1, 1)
# new_predictions = model.predict(new_data)
# print("Predictions on new data:", new_predictions)
# joblib.dump(model, 'linear_regression_model.joblib')
# print("Model saved successfully!")

loaded_model = joblib.load('linear_regression_model.joblib')
print("Model loaded successfully!")
ans = np.array(int(input("Enter a number for the model! ")))
print(f"The models prediction is: {loaded_model.predict(ans.reshape(-1, 1))}")

# The dump does include the scaler, and you dont need to add any code.

# 3
# The ridge, as one of its main functions is preventing overfitting.
# The lasso, as it deletes insignificant features that "hold back" the model.

# 4
# Left to the lines is the under fit, right to the lines is overfit, and the ideal area is between them.
