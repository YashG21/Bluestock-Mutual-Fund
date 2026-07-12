import requests
import pandas as pd
import os

# Folder to save files
output_folder = "data/raw/live_nav"
os.makedirs(output_folder, exist_ok=True)

# Scheme Name : AMFI Code
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    print(f"\nFetching {name}...")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        file_name = f"{output_folder}/{name}.csv"

        df.to_csv(file_name, index=False)

        print(f"✔ Saved: {file_name}")

    else:

        print(f"❌ Failed to fetch {name}")
        