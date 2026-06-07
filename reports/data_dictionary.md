# Mutual Fund Analytics Data Dictionary

## dim_fund

| Column | Description |
|----------|----------|
| amfi_code | Unique fund identifier |
| fund_house | Fund company name |
| scheme_name | Mutual fund scheme name |
| category | Fund category |
| sub_category | Fund sub category |
| plan | Direct/Regular plan |
| launch_date | Scheme launch date |
| benchmark | Benchmark index |
| expense_ratio_pct | Expense ratio percentage |
| exit_load_pct | Exit load percentage |
| min_sip_amount | Minimum SIP amount |
| min_lumpsum_amount | Minimum lump sum amount |
| fund_manager | Fund manager |
| risk_category | Risk category |
| sebi_category_code | SEBI category code |

## fact_nav

| Column | Description |
|----------|----------|
| amfi_code | Fund identifier |
| nav_date | NAV date |
| nav | Net Asset Value |
| daily_return | Daily return percentage |

## fact_transactions

| Column | Description |
|----------|----------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| amfi_code | Fund identifier |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| kyc_status | KYC status |

## fact_performance

Performance metrics such as returns, alpha, beta, Sharpe ratio, Sortino ratio, AUM and risk grade.

## fact_aum

AUM data by fund house.

## fact_sip

Monthly SIP inflow statistics.

## fact_category_inflows

Category-wise inflow information.

## fact_folio

Industry folio statistics.

## fact_holdings

Portfolio stock holdings and sector allocation.

## fact_benchmark

Benchmark index historical values.