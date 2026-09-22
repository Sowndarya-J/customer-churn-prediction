import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

churn_by_contract = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize="index"
) * 100

print(churn_by_contract.round(2))