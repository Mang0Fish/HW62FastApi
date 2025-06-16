import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# שלב 1: הכנסת הנתונים
x = np.array([[30], [35], [40], [45], [50], [55], [60], [65], [70], [75], [80], [85], [90]], dtype=float)
y = np.array([[0], [0], [0], [0], [0], [1], [0], [1], [1], [1], [1], [1], [1]], dtype=float)

# שלב 2: נורמליזציה
# StandardScaler
scaler = StandardScaler()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
scaled_x_train =scaler.fit_transform(x_train)
scaled_x_test = scaler.transform(x_test)

# שלב 3: בניית המודל
ann = Sequential()
ann.add(Dense(units=10, activation='relu'))

# Second layer - Hidden layer
ann.add(Dense(units=10, activation='relu'))

# Third layer - Output layer
ann.add(Dense(units=1, activation='sigmoid'))

# שלב 4: קומפילציה ואימון
ann.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

ann.fit(scaled_x_train, y_train, batch_size=32, epochs=100)

# הסתברות החזר ל-58 אלף ש"ח
income_58 = scaler.transform(np.array([[58]]))
the_pred = ann.predict(income_58)
print(f"The chance is {(the_pred[0][0] * 100):.2f}%")
