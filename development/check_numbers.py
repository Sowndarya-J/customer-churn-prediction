import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

print("Numerical columns:")
print(df[["tenure", "MonthlyCharges", "TotalCharges"]].describe())