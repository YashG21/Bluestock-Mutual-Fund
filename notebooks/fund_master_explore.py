import pandas as pd

# Read the fund master dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 60)
print("FUND MASTER EXPLORATION")
print("=" * 60)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nUnique Categories:")
print(df["category"].unique())

print("\nUnique Sub Categories:")
print(df["sub_category"].unique())

print("\nUnique Risk Grades:")
print(df["risk_category"].unique())