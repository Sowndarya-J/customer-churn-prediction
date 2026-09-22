import sqlite3

connection = sqlite3.connect("customer_churn.db")
cursor = connection.cursor()

query = """
SELECT
    PaymentMethod,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_percentage
FROM customer_data
GROUP BY PaymentMethod
ORDER BY churn_percentage DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(
        "Payment Method:", row[0],
        "| Total:", row[1],
        "| Churned:", row[2],
        "| Churn %:", row[3], "%"
    )

connection.close()