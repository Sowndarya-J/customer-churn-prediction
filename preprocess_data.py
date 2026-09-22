import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing TotalCharges
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Remove customer ID
df = df.drop("customerID", axis=1)

# Convert target column
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Separate input features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Convert categorical columns into numeric columns
X = pd.get_dummies(X, drop_first=True)

print("Original columns:", df.shape[1])
print("Feature columns after encoding:", X.shape[1])

print("\nFirst 5 rows of encoded data:")
print(X.head())

print("\nData types:")
print(X.dtypes)

print("\nTarget:")
print(y.value_counts())