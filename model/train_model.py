import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Example training data
data = {
    "attendance": [60, 70, 80, 90, 85, 75],
    "internal": [20, 25, 30, 35, 32, 28],
    "external": [40, 50, 60, 70, 65, 55]
}

df = pd.DataFrame(data)

X = df[["attendance", "internal"]]
y = df["external"]

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model/model.pkl")

print("Model trained and saved")