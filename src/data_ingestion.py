import pandas as pd

# Dataset 1
fund_master = pd.read_csv(r"../data/raw/01_fund_master.csv")
print("\n===== FUND MASTER =====")
print(fund_master.shape)
print(fund_master.dtypes)
print(fund_master.head())

# Dataset 2
nav_history = pd.read_csv(r"../data/raw/02_nav_history.csv")
print("\n===== NAV HISTORY =====")
print(nav_history.shape)
print(nav_history.dtypes)
print(nav_history.head())

# Dataset 3
aum = pd.read_csv(r"../data/raw/03_aum_by_fund_house.csv")
print("\n===== AUM BY FUND HOUSE =====")
print(aum.shape)
print(aum.dtypes)
print(aum.head())

# Dataset 4
sip = pd.read_csv(r"../data/raw/04_monthly_sip_inflows.csv")
print("\n===== SIP INFLOWS =====")
print(sip.shape)
print(sip.dtypes)
print(sip.head())

# Dataset 5
category_inflows = pd.read_csv(r"../data/raw/05_category_inflows.csv")
print("\n===== CATEGORY INFLOWS =====")
print(category_inflows.shape)
print(category_inflows.dtypes)
print(category_inflows.head())

# Dataset 6
folio = pd.read_csv(r"../data/raw/06_industry_folio_count.csv")
print("\n===== INDUSTRY FOLIO COUNT =====")
print(folio.shape)
print(folio.dtypes)
print(folio.head())

# Dataset 7
performance = pd.read_csv(r"../data/raw/07_scheme_performance.csv")
print("\n===== SCHEME PERFORMANCE =====")
print(performance.shape)
print(performance.dtypes)
print(performance.head())

# Dataset 8
transactions = pd.read_csv(r"../data/raw/08_investor_transactions.csv")
print("\n===== INVESTOR TRANSACTIONS =====")
print(transactions.shape)
print(transactions.dtypes)
print(transactions.head())

# Dataset 9
holdings = pd.read_csv(r"../data/raw/09_portfolio_holdings.csv")
print("\n===== PORTFOLIO HOLDINGS =====")
print(holdings.shape)
print(holdings.dtypes)
print(holdings.head())

# Dataset 10
benchmark = pd.read_csv(r"../data/raw/10_benchmark_indices.csv")
print("\n===== BENCHMARK INDICES =====")
print(benchmark.shape)
print(benchmark.dtypes)
print(benchmark.head())

print("\nAll datasets loaded successfully.")