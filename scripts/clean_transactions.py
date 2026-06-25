import pandas as pd
import os

print("=" * 60)
print("Cleaning Investor Transactions")
print("=" * 60)

# Load CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid_types = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid_types)]

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC Status
df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = ["Verified", "Pending"]

df = df[df["kyc_status"].isin(valid_kyc)]

print("Cleaned Shape:", df.shape)

# Save
os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("File Saved Successfully")