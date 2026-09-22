-- Customer Churn SQL Analysis
-- Project: Customer Churn Prediction & Risk Scoring


-- 1. Total number of customers
SELECT COUNT(*) AS total_customers
FROM customer_data;


-- 2. Total number of churned customers
SELECT COUNT(*) AS churned_customers
FROM customer_data
WHERE Churn = 'Yes';


-- 3. Customer count and churn count by contract
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_data
GROUP BY Contract;


-- 4. Churn percentage by contract
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_percentage
FROM customer_data
GROUP BY Contract;


-- 5. Average monthly charges
SELECT
    ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges
FROM customer_data;


-- 6. Average monthly charges by churn status
SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS average_monthly_charges
FROM customer_data
GROUP BY Churn;


-- 7. Churn percentage by internet service
SELECT
    InternetService,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_percentage
FROM customer_data
GROUP BY InternetService;


-- 8. Churn percentage by payment method
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