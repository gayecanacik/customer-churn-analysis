import pandas as pd

df = pd.read_csv("/Users/gayecanacik/Desktop/customer_churn_dataset-testing-master.csv")
print(df.head())
print(df.shape)
print(df.info())

print(df.groupby("Churn")["Age"].mean())

print(df.groupby('Churn')['Tenure'].mean())
print(df.groupby("Churn")["Usage Frequency"].mean())
print(df.groupby("Churn")["Support Calls"].mean())
print(df.groupby("Churn")["Payment Delay"].mean())

print(df.corr(numeric_only=True)["Churn"].sort_values(ascending=False))

print("\n--- Churned vs Non-Churned Comparison ---")

print(df.groupby("Churn")[[
    "Age",
    "Tenure",
    "Usage Frequency",
    "Support Calls",
    "Payment Delay"
]].mean())

print("\n--- Descriptive Statistics ---")

print(df[[
    "Age",
    "Tenure",
    "Usage Frequency",
    "Support Calls",
    "Payment Delay",
    "Total Spend"
]].describe())

print("\n--- Churn Rate by Subscription Type ---")

print(
    df.groupby("Subscription Type")["Churn"]
    .mean()
    .sort_values(ascending=False)
)

print("\n--- Churn Rate by Contract Length ---")

print(
    df.groupby("Contract Length")["Churn"]
    .mean()
    .sort_values(ascending=False)
)

import matplotlib.pyplot as plt

churn_by_contract = df.groupby("Contract Length")["Churn"].mean()

churn_by_contract.plot(kind="bar")

plt.title("Churn Rate by Contract Length")
plt.xlabel("Contract Length")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.show()

print("\n--- Churn Rate by Subscription Type ---")

churn_by_subscription = df.groupby("Subscription Type")["Churn"].mean()

churn_by_subscription.plot(kind="bar")

plt.title("Churn Rate by Subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.show()

print("\n--- Churn Rate by Support Calls ---")

churn_by_support = df.groupby("Support Calls")["Churn"].mean()

churn_by_support.plot(kind="bar")

plt.title("Churn Rate by Number of Support Calls")
plt.xlabel("Number of Support Calls")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.show()

print("\n--- Churn Rate by Payment Delay ---")

churn_by_payment = df.groupby("Payment Delay")["Churn"].mean()

churn_by_payment.plot(kind="line")

plt.title("Churn Rate by Payment Delay")
plt.xlabel("Payment Delay (Days)")
plt.ylabel("Churn Rate")
plt.show()

print("\n--- Key Findings ---")

print("1. Monthly contracts have the highest churn rate.")
print("2. Higher payment delays are associated with higher churn.")
print("3. Churned customers have more support calls on average.")
print("4. Churned customers have lower usage frequency on average.")

churn_by_contract.plot(kind="bar")

plt.title("Churn Rate by Contract Length")
plt.xlabel("Contract Length")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.savefig("/Users/gayecanacik/Desktop/churn_by_contract.png", bbox_inches="tight")
plt.show()

churn_by_subscription.plot(kind="bar")

plt.title("Churn Rate by Subscription Type")
plt.xlabel("Subscription Type")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.savefig("/Users/gayecanacik/Desktop/churn_by_subscription.png", bbox_inches="tight")
plt.show()

churn_by_support.plot(kind="bar")

plt.title("Churn Rate by Number of Support Calls")
plt.xlabel("Number of Support Calls")
plt.ylabel("Churn Rate")
plt.xticks(rotation=0)
plt.savefig("/Users/gayecanacik/Desktop/churn_by_support.png", bbox_inches="tight")
plt.show()

churn_by_payment.plot(kind="line")

plt.title("Churn Rate by Payment Delay")
plt.xlabel("Payment Delay (Days)")
plt.ylabel("Churn Rate")
plt.savefig("/Users/gayecanacik/Desktop/churn_by_payment.png", bbox_inches="tight")
plt.show()