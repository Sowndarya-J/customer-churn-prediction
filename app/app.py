import streamlit as st
import pandas as pd
import joblib


# =========================================================
# 1. LOAD MODEL AND SCALER
# =========================================================

model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")


# =========================================================
# 2. PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)


# =========================================================
# 3. TITLE
# =========================================================

st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer details to predict the probability of churn."
)


# =========================================================
# 4. CUSTOMER INPUTS
# =========================================================

tenure = st.number_input(
    "Tenure (months)",
    min_value=0,
    max_value=72,
    value=2
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=95.50
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=191.00
)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior_citizen = st.selectbox(
    "Senior Citizen",
    [0, 1]
)

partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)

phone_service = st.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

multiple_lines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

online_security = st.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

online_backup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

streaming_tv = st.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

streaming_movies = st.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


# =========================================================
# 5. PREDICTION BUTTON
# =========================================================

if st.button("🔍 Predict Churn"):

    # Create customer dictionary
    customer = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    # Convert to DataFrame
    customer_df = pd.DataFrame([customer])

    # One-hot encoding
    customer_df = pd.get_dummies(
        customer_df,
        drop_first=True
    )

    # Match training features
    training_features = model.feature_names_in_

    for column in training_features:
        if column not in customer_df.columns:
            customer_df[column] = 0

    customer_df = customer_df[
        training_features
    ]

    # Convert to integer
    customer_df = customer_df.astype(int)

    # Scale numerical columns
    numerical_columns = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    customer_df[numerical_columns] = scaler.transform(
        customer_df[numerical_columns]
    )

    # Predict probability
    probability = model.predict_proba(
        customer_df
    )[:, 1][0]

    percentage = probability * 100

    # Risk level
    if percentage <= 30:
        risk = "Low Risk"

    elif percentage <= 70:
        risk = "Medium Risk"

    else:
        risk = "High Risk"

    # Display results
    st.subheader("Prediction Result")

    st.metric(
        "Churn Probability",
        f"{percentage:.2f}%"
    )

    st.write(
        f"### Risk Level: {risk}"
    )