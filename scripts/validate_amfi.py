import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

missing = set(fund["amfi_code"]) - set(nav["amfi_code"])

print("=" * 50)
print("AMFI CODE VALIDATION")
print("=" * 50)

if len(missing) == 0:
    print("✅ All AMFI codes exist in nav_history.csv")
else:
    print("❌ Missing Codes:")
    print(missing)