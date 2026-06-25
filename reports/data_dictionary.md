# Data Dictionary

## dim_fund

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Scheme Name |
| fund_house | TEXT | AMC Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| risk_category | TEXT | Risk Level |

---

## fact_nav

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | INTEGER | Transaction ID |
| investor_id | INTEGER | Investor ID |
| amfi_code | INTEGER | Scheme Code |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Investment Amount |
| state | TEXT | Investor State |
| kyc_status | TEXT | KYC Verification Status |

---

## fact_performance

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| return_1yr_pct | REAL | One Year Return |
| return_3yr_pct | REAL | Three Year Return |
| return_5yr_pct | REAL | Five Year Return |
| expense_ratio_pct | REAL | Expense Ratio |

---

## fact_aum

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| aum_cr | REAL | Assets Under Management (Crores) |
| report_date | DATE | Report Date |