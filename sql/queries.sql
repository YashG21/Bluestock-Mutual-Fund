-- 1. Top 5 funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_cr DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
strftime('%Y-%m', date) AS Month,
AVG(nav) AS Average_NAV
FROM fact_nav
GROUP BY Month
ORDER BY Month;

-- 3. SIP Transactions
SELECT COUNT(*) AS SIP_Count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4. Transactions by State
SELECT
state,
COUNT(*) AS Total_Transactions
FROM fact_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT
amfi_code,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Expense Ratio
SELECT
AVG(expense_ratio_pct)
FROM fact_performance;

-- 7. Highest NAV
SELECT
MAX(nav)
FROM fact_nav;

-- 8. Lowest NAV
SELECT
MIN(nav)
FROM fact_nav;

-- 9. Number of Funds by Category
SELECT
category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10. Total Transaction Amount
SELECT
SUM(amount_inr)
FROM fact_transactions;