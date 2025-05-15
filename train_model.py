import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Generate dummy data
np.random.seed(42)
height = np.random.normal(170, 10, 300)
weight = np.random.normal(70, 15, 300)
X = np.column_stack((height, weight))
y = (weight / ((height / 100) ** 2) > 30).astype(int)

# Scale + Train
X_train, X_test, y_train, y_test = train_test_split(X, y)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_scaled, y_train)

# Save
joblib.dump((scaler, model), "model/obesity_classifier.pkl")
