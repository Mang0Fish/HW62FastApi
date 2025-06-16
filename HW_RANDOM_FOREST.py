from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# large data set
x, y = make_classification(n_samples=10000, n_features=20, n_informative=15,
                           n_redundant=5, n_classes=2, random_state=42)

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size=0.3, random_state=42)

decision = DecisionTreeClassifier(random_state=42)
random = RandomForestClassifier(n_estimators=100, random_state=42)

decision.fit(xTrain, yTrain)
random.fit(xTrain, yTrain)

decisionPred = decision.predict(xTest)
randomPred = random.predict(xTest)

decisionAcc = accuracy_score(yTest, decisionPred)
randomAcc = accuracy_score(yTest, randomPred)

print("DecisionTree Accuracy:", decisionAcc,"RandomForest Accuracy:", randomAcc)

model = ["Decision Tree", "Random Forest"]
accuracy = [decisionAcc, randomAcc]
plt.bar(model, accuracy, color = ['green', 'olive'])
plt.title("DecisionTree VS RandomForest")
plt.ylabel("Accuracy")
plt.xlabel("Model")
plt.grid()
plt.show()
