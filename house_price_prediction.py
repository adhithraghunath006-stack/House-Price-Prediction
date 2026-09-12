import pandas as pd

# Load the dataset
df = pd.read_csv("train.csv")

# Display first 5 rows
print(df.head())

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

# Select features and target
features = ["GrLivArea", "BedroomAbvGr", "FullBath", "YearBuilt"]

X = df[features]
y = df["SalePrice"]

print("\nSelected Features:")
print(X.head())

print("\nTarget (SalePrice):")
print(y.head())
from sklearn.model_selection import train_test_split

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data shape:")
print(X_train.shape)

print("\nTesting data shape:")
print(X_test.shape)

from sklearn.linear_model import LinearRegression

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")

# Predict house prices using the trained model
y_pred = model.predict(X_test)

print("\nPredicted House Prices:")
print(y_pred[:10])

from sklearn.metrics import r2_score

# Calculate R² score
r2 = r2_score(y_test, y_pred)

print("\nR² Score:")
print(r2)

import matplotlib.pyplot as plt

# Plot Actual vs Predicted house prices
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.6)

# Perfect prediction reference line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")

plt.tight_layout()

# Save the plot
plt.savefig("actual_vs_predicted.png")

plt.show()

# Save actual and predicted prices
results = pd.DataFrame({
    "ActualPrice": y_test,
    "PredictedPrice": y_pred
})

results.to_csv("prediction_results.csv", index=False)

print("\nPrediction results saved as prediction_results.csv")