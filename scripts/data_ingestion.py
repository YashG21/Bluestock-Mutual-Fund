import os
import pandas as pd

# Path to raw data
raw_path = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(raw_path) if f.endswith(".csv")]

print("=" * 60)
print("BLUESTOCK DATA INGESTION")
print("=" * 60)

# Loop through all CSV files
for file in csv_files:

    file_path = os.path.join(raw_path, file)

    print("\n" + "=" * 60)
    print(f"Reading File: {file}")
    print("=" * 60)

    try:
        df = pd.read_csv(file_path)

        print("Shape:", df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except Exception as e:
        print("Error:", e)