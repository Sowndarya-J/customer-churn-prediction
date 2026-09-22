import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing values
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Remove customer ID
df = df.drop("customerID", axis=1)

# Convert target
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Separate features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# One-hot encode categorical columns
X = pd.get_dummies(X, drop_first=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Total rows:", len(X))
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

print("\nTraining churn distribution:")
print(y_train.value_counts())

print("\nTesting churn distribution:")
print(y_test.value_counts())