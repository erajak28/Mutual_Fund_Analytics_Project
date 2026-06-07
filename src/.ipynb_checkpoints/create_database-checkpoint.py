import pandas as pd
from sqlalchemy import create_engine

# SQLite database connection
engine = create_engine("sqlite:///../bluestock_mf.db")

# Processed data folder
processed_path = "C:/Users/WINDOWS/OneDrive/Documents/Mutual_Fund_Analytics_Project/data/processed/"

# Read cleaned CSV files
fund_master = pd.read_csv(processed_path + "clean_fund_master.csv")
nav = pd.read_csv(processed_path + "clean_nav.csv")
transactions = pd.read_csv(processed_path + "clean_transactions.csv")
performance = pd.read_csv(processed_path + "clean_performance.csv")
aum = pd.read_csv(processed_path + "clean_aum_by_fund_house.csv")
sip = pd.read_csv(processed_path + "clean_monthly_sip_inflows.csv")
category_inflows = pd.read_csv(processed_path + "clean_category_inflows.csv")
folio = pd.read_csv(processed_path + "clean_industry_folio_count.csv")
holdings = pd.read_csv(processed_path + "clean_portfolio_holdings.csv")
benchmark = pd.read_csv(processed_path + "clean_benchmark_indices.csv")

# Rename date column in NAV to match schema.sql
nav = nav.rename(columns={"date": "nav_date"})

# Create daily return column for NAV
nav["daily_return"] = nav.groupby("amfi_code")["nav"].pct_change() * 100

# Load data into SQLite tables
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

# Additional cleaned datasets
sip.to_sql("fact_sip", engine, if_exists="replace", index=False)
category_inflows.to_sql("fact_category_inflows", engine, if_exists="replace", index=False)
folio.to_sql("fact_folio", engine, if_exists="replace", index=False)
holdings.to_sql("fact_holdings", engine, if_exists="replace", index=False)
benchmark.to_sql("fact_benchmark", engine, if_exists="replace", index=False)

print("SQLite database created successfully.")
print("Database file: bluestock_mf.db")
print("10 cleaned datasets loaded into SQLite tables.")