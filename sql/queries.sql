-- 1. Top 5 fund houses by AUM
SELECT 
    fund_house,
    ROUND(SUM(aum_crore), 2) AS total_aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;


-- 2. Average NAV per month
SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', nav_date)
ORDER BY month;


-- 3. SIP inflow YoY growth
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip
ORDER BY month;


-- 4. Transactions by state
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr
FROM fact_transactions
GROUP BY state
ORDER BY total_amount_inr DESC;


-- 5. Funds with expense ratio less than 1%
SELECT
    scheme_name,
    fund_house,
    category,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct ASC;


-- 6. Transaction type distribution
SELECT
    transaction_type,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;


-- 7. Top 10 funds by 5-year return
SELECT
    scheme_name,
    fund_house,
    category,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 8. Top 10 funds by Sharpe ratio
SELECT
    scheme_name,
    fund_house,
    category,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 9. Portfolio market value by sector
SELECT
    sector,
    ROUND(SUM(market_value_cr), 2) AS total_market_value_cr
FROM fact_holdings
GROUP BY sector
ORDER BY total_market_value_cr DESC;


-- 10. Benchmark average close value by index
SELECT
    index_name,
    ROUND(AVG(close_value), 2) AS avg_close_value,
    ROUND(MAX(close_value), 2) AS max_close_value,
    ROUND(MIN(close_value), 2) AS min_close_value
FROM fact_benchmark
GROUP BY index_name
ORDER BY avg_close_value DESC;