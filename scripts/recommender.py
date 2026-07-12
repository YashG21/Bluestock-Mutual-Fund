import pandas as pd

# Load the scheme performance dataset
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

print("=" * 60)
print("      Mutual Fund Recommendation System")
print("=" * 60)

print("\nAvailable Risk Levels:")
print("1. Low")
print("2. Moderate")
print("3. Moderately High")
print("4. High")
print("5. Very High")

risk = input("\nEnter your Risk Appetite: ").strip()

# Filter funds by risk grade
recommended = performance[
    performance["risk_grade"].str.lower() == risk.lower()
]

# Sort by Sharpe Ratio
recommended = recommended.sort_values(
    by="sharpe_ratio",
    ascending=False
)

# Select Top 3 Funds
top3 = recommended.head(3)

if top3.empty:
    print("\nNo funds found for the selected risk level.")
else:
    print("\nTop 3 Recommended Funds\n")
    print(
        top3[
             [
            "scheme name",
            "fund house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            ]
        ]
    )