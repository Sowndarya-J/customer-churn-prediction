import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Contract types:")
print(df["Contract"].value_counts())

print("\nInternet services:")
print(df["InternetService"].value_counts())

print("\nPayment methods:")
print(df["PaymentMethod"].value_counts())

print("\nTech support:")
print(df["TechSupport"].value_counts())

print("\nChurn:")
print(df["Churn"].value_counts())