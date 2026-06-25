import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("Database Created Successfully")

# Load cleaned CSVs
nav = pd.read_csv("data/processed/clean_nav_history.csv")
transactions = pd.read_csv("data/processed/clean_investor_transactions.csv")
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

fund = pd.read_csv("data/raw/01_fund_master.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Save tables
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("All Tables Loaded Successfully")

# Verify row counts
tables = {
    "dim_fund": fund,
    "fact_nav": nav,
    "fact_transactions": transactions,
    "fact_performance": performance,
    "fact_aum": aum
}

print("\nRow Count Verification")
print("-" * 40)

for name, df in tables.items():
    print(f"{name}: {len(df)} rows")