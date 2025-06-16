import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import numpy as np

# Dataset
data = pd.DataFrame({
    'Discount': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No'],
    'Purchase': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No'],
    'Returned': ['Yes', 'No', 'Yes', 'No', 'Yes', 'No']
})
x = pd.get_dummies(data[['Discount', 'Purchase']])
clf = DecisionTreeClassifier(criterion='gini', random_state=42)
y = (data['Returned'] == 'Yes').astype(int)
clf.fit(x, y)
customer = pd.DataFrame([[0,1,1,0]], columns=x.columns)
customer_pred = clf.predict(customer)
print(customer_pred)

plot_tree(clf)
plt.show()

clf_entropy = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf_entropy.fit(x, y)
plot_tree(clf_entropy)
plt.show()

