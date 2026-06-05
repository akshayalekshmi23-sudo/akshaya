import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Score': [35, 40, 50, 55, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

# Input and output
X = df[['Study_Hours']]
y = df['Score']

# Train model
model = LinearRegression()
model.fit(X, y)

# User input
hours = float(input("Enter study hours: "))

# Prediction
predicted_score = model.predict([[hours]])

print(f"Predicted Score: {predicted_score[0]:.2f}")