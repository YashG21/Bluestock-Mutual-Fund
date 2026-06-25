import pandas as pd
import os

print("=" * 60)
print("Cleaning Scheme Performance")
print("=" * 60)

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Expense ratio validation
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

print("Cleaned Shape:", df.shape)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("File Saved Successfully")