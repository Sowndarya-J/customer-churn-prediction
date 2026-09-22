# Snapshots Directory

This directory contains snapshots of your code for AI interactions. Each snapshot is a markdown file that includes relevant code context and project structure information.

## What's included in snapshots?
- Selected code files and their contents
- Project structure (if enabled)
- Your prompt/question for the AI

## Configuration
You can customize snapshot behavior in `config.json`.
## Model Training & Evaluation

Two classification models were evaluated:

1. Logistic Regression
2. Random Forest

### Logistic Regression

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 80.70% |
| Precision | 66.04% |
| Recall    | 56.15% |
| F1 Score  | 60.69% |
| ROC-AUC   | 84.23% |

### Random Forest

| Metric    | Result |
| --------- | -----: |
| Accuracy  | 78.50% |
| Precision | 62.03% |
| Recall    | 48.93% |
| F1 Score  | 54.71% |
| ROC-AUC   | 82.26% |

### Selected Model

Logistic Regression was selected for the current project version because it achieved better results than Random Forest on the evaluated test set across the reported metrics.

## Confusion Matrix

The Logistic Regression model produced the following confusion matrix:

```text
                 Predicted
              No Churn   Churn

Actual
No Churn         927       108
Churn            164       210
```

The confusion matrix is also available at:

`results/confusion_matrix.png`
## SQL Analysis Results

The following observations were obtained from the customer dataset using SQLite queries.

### Customer Overview

* Total customers: **7,043**
* Total churned customers: **1,869**

### Contract Type

| Contract       | Churn Rate |
| -------------- | ---------: |
| Month-to-month |     42.71% |
| One year       |     11.27% |
| Two year       |      2.83% |

### Monthly Charges

* Overall average monthly charge: **64.76**
* Average monthly charge for non-churned customers: **61.27**
* Average monthly charge for churned customers: **74.44**

### Internet Service

| Internet Service    | Churn Rate |
| ------------------- | ---------: |
| DSL                 |     18.96% |
| Fiber optic         |     41.89% |
| No internet service |      7.40% |

### Payment Method

| Payment Method            | Churn Rate |
| ------------------------- | ---------: |
| Electronic check          |     45.29% |
| Mailed check              |     19.11% |
| Bank transfer (automatic) |     16.71% |
| Credit card (automatic)   |     15.24% |

These results represent associations observed in the dataset and should not be interpreted as proof that a particular customer characteristic directly causes churn.
