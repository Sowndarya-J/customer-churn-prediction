import pandas as pd
import sqlite3


# Load CSV dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Connect to SQLite database
connection = sqlite3.connect("customer_churn.db")

# Store CSV data as a database table
df.to_sql(
    "customer_data",
    connection,
    if_exists="replace",
    index=False
)

# Close connection
connection.close()

print("Database created successfully!")
print("Table created: customer_data")