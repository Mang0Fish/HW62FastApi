from sklearn.linear_model import LogisticRegression
import numpy as np
import math

x = np.array([30,35,40,45,50,55,60,65,70,75,80,85,90]).reshape(-1, 1)
y = np.array([0,0,0,0,0,1,0,1,1,1,1,1,1])

# Exercise 1
# 1
logModel = LogisticRegression(solver="liblinear")
logModel.fit(x, y)

# 2
res = logModel.predict_proba(np.array([58]).reshape(-1, 1))[-1, -1] * 100

print(f"The probability is {res:.1f}%")

# 3
b0 = logModel.intercept_[0]
b1 = logModel.coef_[0][0]


def get_threshold(probability):
    logit = math.log(probability / (1 - probability))
    return (logit - b0) / b1

res = get_threshold(0.75)
print(f"The minimum salary is {res:.2f}")

# Exercise 2
import pandas as pd

# 1
aparts = pd.read_csv(r"C:\Users\User\Downloads\apartments.csv")
aparts = pd.DataFrame(aparts)
print(aparts)

# 2
x = np.array(aparts[['area', 'rooms', 'age', 'distance']])
y = np.array(aparts['type'])
print(x, y)

# 3
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 4
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 5
linModel = LogisticRegression(multi_class="multinomial", solver="lbfg", C=5)
logModel.fit(x_train_scaled, y_train)

# 6
from sklearn.metrics import accuracy_score, confusion_matrix
y_pred = logModel.predict(x_test_scaled)
print(accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print(cm)
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(data=cm, annot=True, xticklabels=[0,1,2,3], yticklabels=[0,1,2,3])
plt.xlabel("Predicted")
plt.ylabel("True")
plt.title("Confusion Matrix Heatmap")
plt.show()
apartment = np.array([90, 4, 10, 4]).reshape(1, -1)
apartment_scaled = scaler.transform(apartment)
pred = logModel.predict(apartment_scaled)
print(pred)