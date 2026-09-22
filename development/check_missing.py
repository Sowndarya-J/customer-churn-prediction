import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Missing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nChurn count:")
print(df["Churn"].value_counts())