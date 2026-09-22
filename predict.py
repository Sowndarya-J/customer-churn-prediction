import pandas as pd
import joblib


# =========================================================
# 1. LOAD SAVED MODEL AND SCALER
# =========================================================

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# =========================================================
# 2. CREATE NEW CUSTOMER DATA
# =========================================================

customer = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 2,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 95.50,
    "TotalCharges": 191.00
}


# Convert dictionary to DataFrame
customer_df = pd.DataFrame([customer])


# =========================================================
# 3. ONE-HOT ENCODING
# =========================================================

customer_df = pd.get_dummies(
    customer_df,
    drop_first=True
)


# =========================================================
# 4. MATCH TRAINING FEATURES
# =========================================================

# Get the feature names used during model training
training_features = model.feature_names_in_

# Add missing columns
for column in training_features:

    if column not in customer_df.columns:
        customer_df[column] = 0


# Remove any extra columns
customer_df = customer_df[
    training_features
]


# =========================================================
# 5. CONVERT DATA TYPES
# =========================================================

customer_df = customer_df.astype(int)


# =========================================================
# 6. SCALE NUMERICAL FEATURES
# =========================================================

numerical_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

customer_df[numerical_columns] = scaler.transform(
    customer_df[numerical_columns]
)


# =========================================================
# 7. PREDICT CHURN
# =========================================================

churn_probability = model.predict_proba(
    customer_df
)[:, 1][0]


churn_percentage = churn_probability * 100


# =========================================================
# 8. DETERMINE RISK LEVEL
# =========================================================

if churn_percentage <= 30:
    risk = "Low Risk"

elif churn_percentage <= 70:
    risk = "Medium Risk"

else:
    risk = "High Risk"


# =========================================================
# 9. DISPLAY RESULT
# =========================================================

print("\nCustomer Churn Prediction")
print("---------------------------")

print(
    "Churn Probability:",
    round(churn_percentage, 2),
    "%"
)

print(
    "Risk Level:",
    risk
)