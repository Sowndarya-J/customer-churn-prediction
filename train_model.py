import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


# =========================================================
# 1. LOAD DATASET
# =========================================================

df = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Dataset loaded successfully!")
print("Total rows:", len(df))


# =========================================================
# 2. DATA CLEANING
# =========================================================

# Convert TotalCharges from text to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Fill missing TotalCharges values
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# Remove customer ID because it is not useful for prediction
df = df.drop("customerID", axis=1)

# Convert target variable
# No = 0
# Yes = 1
df["Churn"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})


# =========================================================
# 3. SEPARATE FEATURES AND TARGET
# =========================================================

X = df.drop("Churn", axis=1)
y = df["Churn"]


# =========================================================
# 4. ENCODE CATEGORICAL VARIABLES
# =========================================================

X = pd.get_dummies(
    X,
    drop_first=True
)

print("Number of features after encoding:", X.shape[1])


# =========================================================
# 5. TRAIN-TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# =========================================================
# 6. CONVERT DATA TYPES
# =========================================================

X_train = X_train.astype(int)
X_test = X_test.astype(int)


# =========================================================
# 7. FEATURE SCALING
# =========================================================

scaler = StandardScaler()

numerical_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

X_train[numerical_columns] = scaler.fit_transform(
    X_train[numerical_columns]
)

X_test[numerical_columns] = scaler.transform(
    X_test[numerical_columns]
)


# =========================================================
# 8. TRAIN LOGISTIC REGRESSION MODEL
# =========================================================

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

print("\nModel training completed!")


# =========================================================
# 9. SAVE MODEL AND SCALER
# =========================================================

joblib.dump(
    model,
    "models/churn_model.pkl"
)

joblib.dump(
    scaler,
    "models/scaler.pkl"
)

print("Model saved: models/churn_model.pkl")
print("Scaler saved: models/scaler.pkl")


# =========================================================
# 10. MAKE PREDICTIONS
# =========================================================

y_pred = model.predict(X_test)

# Probability of churn
y_probability = model.predict_proba(X_test)[:, 1]


# =========================================================
# 11. MODEL EVALUATION
# =========================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_probability
)


print("\nModel Evaluation:")
print("---------------------------")

print(
    "Accuracy :",
    round(accuracy * 100, 2),
    "%"
)

print(
    "Precision:",
    round(precision * 100, 2),
    "%"
)

print(
    "Recall   :",
    round(recall * 100, 2),
    "%"
)

print(
    "F1 Score :",
    round(f1 * 100, 2),
    "%"
)

print(
    "ROC-AUC  :",
    round(roc_auc * 100, 2),
    "%"
)


# =========================================================
# 12. CONFUSION MATRIX
# =========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")
print(cm)

print("\nTN:", cm[0, 0])
print("FP:", cm[0, 1])
print("FN:", cm[1, 0])
print("TP:", cm[1, 1])


# =========================================================
# 13. CREATE CONFUSION MATRIX IMAGE
# =========================================================

plt.figure(figsize=(6, 5))

plt.imshow(cm)

plt.title(
    "Customer Churn - Confusion Matrix"
)

plt.xlabel(
    "Predicted"
)

plt.ylabel(
    "Actual"
)

plt.xticks(
    [0, 1],
    ["No Churn", "Churn"]
)

plt.yticks(
    [0, 1],
    ["No Churn", "Churn"]
)


# Display numbers inside the matrix
for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )


plt.tight_layout()

plt.savefig(
    "results/confusion_matrix.png"
)

plt.close()

print(
    "\nConfusion matrix saved: "
    "results/confusion_matrix.png"
)


# =========================================================
# 14. FINAL MESSAGE
# =========================================================

print(
    "\nTraining and model evaluation "
    "completed successfully!"
)