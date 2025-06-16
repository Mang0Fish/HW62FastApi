import numpy as np
import math

from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

age = np.array([22, 25, 30, 35, 42, 50, 23, 28, 33, 48])
salary = np.array([60, 75, 80, 120, 150, 110, 95, 90, 105, 135])
credit = np.array([1, 2, 3, 5, 8, 10, 1, 2, 4, 9])
y = np.array(['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes'])
x = np.column_stack((age, salary, credit))

# 1
scaler = MinMaxScaler()
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=42)
scaler.fit(xTrain)
xTrainScaled = scaler.transform(xTrain)
xTestScaled = scaler.transform(xTest)

# 2
model = KNeighborsClassifier(3)
model.fit(xTrainScaled, yTrain)
yPred = model.predict(xTestScaled)
print("Accuracy score: ",accuracy_score(yTest, yPred))
customer = np.array([[27, 95, 3]])
customer = scaler.transform(customer)
customerPred = model.predict(customer)
print(customerPred)

# 3
customerProba = model.predict_proba(customer)
class_names = model.classes_
print("\nClasses:")
for cls, prob in zip(class_names, customerProba[0]):
    print(f"{int(3*prob)} {cls}")

# 4
# My models forecast is 'No', because more neighbors were 'No' than 'Yes'