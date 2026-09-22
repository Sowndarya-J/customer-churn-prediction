import pandas as pd

df = pd.read_csv("data/Telco-Customer-Churn.csv")

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 36, 72],
    labels=["New", "Medium", "Long-term"]
)

churn_by_tenure = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

print(churn_by_tenure.round(2))