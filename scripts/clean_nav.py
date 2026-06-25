import pandas as pd
import os

print("=" * 60)
print("Cleaning NAV History")
print("=" * 60)

# Load CSV
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort records
df = df.sort_values(["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Forward fill NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV
df = df[df["nav"] > 0]

print("Cleaned Shape:", df.shape)

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Save cleaned file
df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("File Saved Successfully")