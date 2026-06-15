# Mutual Fund Analytics & Investor Insights Platform

## Project Overview

This project is an end-to-end Mutual Fund Analytics Platform developed using Python, SQL, SQLite, and Power BI. The objective is to analyze mutual fund performance, investor behavior, SIP trends, and portfolio risk while providing actionable insights through interactive dashboards and advanced analytics.

The project covers the complete analytics lifecycle including data ingestion, cleaning, exploratory analysis, performance evaluation, dashboard development, and advanced financial analytics.

---

# Business Problem

Mutual fund investors and financial institutions require a data-driven approach to evaluate fund performance, monitor investor behavior, assess risk, and identify investment opportunities.

The goal of this project is to:

* Analyze mutual fund industry trends
* Evaluate fund performance using financial metrics
* Study investor transaction behavior
* Monitor SIP growth and continuity
* Build a recommendation framework for investors
* Develop an interactive business dashboard

---

# Project Objectives

1. Build an automated mutual fund analytics pipeline.
2. Clean and transform multiple financial datasets.
3. Analyze industry-wide mutual fund trends.
4. Calculate advanced fund performance metrics.
5. Develop an interactive Power BI dashboard.
6. Perform investor behavior analysis.
7. Build a simple fund recommendation engine.
8. Generate actionable business insights.

---

# Dataset Description

The project uses 10 datasets:

| Dataset               | Description                  |
| --------------------- | ---------------------------- |
| Fund Master           | Scheme details and metadata  |
| NAV History           | Historical NAV data          |
| AUM by Fund House     | Assets under management      |
| Monthly SIP Inflows   | SIP industry statistics      |
| Category Inflows      | Category-wise investments    |
| Industry Folio Count  | Investor folio statistics    |
| Scheme Performance    | Fund return metrics          |
| Investor Transactions | Investor transaction history |
| Portfolio Holdings    | Fund portfolio composition   |
| Benchmark Indices     | NIFTY 50 and NIFTY 100 data  |

---

# Technology Stack

## Programming

* Python
* SQL

## Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

## Database

* SQLite

## Visualization

* Power BI

## Version Control

* Git
* GitHub

---

# Project Architecture

Raw Data
↓
Data Ingestion
↓
Data Cleaning & Validation
↓
SQLite Database
↓
Exploratory Data Analysis
↓
Performance Analytics
↓
Advanced Analytics
↓
Power BI Dashboard
↓
Business Insights

---

# ETL Pipeline

## Extract

Imported raw CSV datasets containing mutual fund and investor data.

## Transform

Performed:

* Missing value handling
* Data type correction
* Duplicate removal
* Date standardization
* Feature engineering
* Data validation

## Load

Loaded cleaned datasets into SQLite database for analysis and dashboard reporting.

---

# Exploratory Data Analysis

Key EDA activities:

* NAV trend analysis
* AUM growth analysis
* SIP inflow analysis
* Category inflow analysis
* Investor demographic analysis
* Geographic investment analysis
* Correlation analysis

Generated visualizations include:

* NAV trends
* AUM growth charts
* SIP inflow trends
* Category heatmaps
* Investor demographics
* Geographic analysis

---

# Performance Analytics

Calculated:

## Return Metrics

* CAGR (1Y, 3Y, 5Y)
* Absolute Returns

## Risk Metrics

* Standard Deviation
* Maximum Drawdown

## Risk-Adjusted Metrics

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta

## Fund Ranking

Generated a composite Fund Scorecard using weighted scoring methodology.

---

# Advanced Analytics

## Historical VaR & CVaR

Measured downside risk for all schemes.

## Rolling Sharpe Ratio

Evaluated changing risk-adjusted performance over time.

## Investor Cohort Analysis

Analyzed investment behavior by investor cohorts.

## SIP Continuity Analysis

Identified at-risk SIP investors using transaction gap analysis.

## Fund Recommendation Engine

Recommended funds based on risk profile and Sharpe Ratio.

## Portfolio Concentration Analysis

Calculated Herfindahl-Hirschman Index (HHI) for portfolio diversification assessment.

---

# Power BI Dashboard

The dashboard contains four pages:

## Page 1 — Industry Overview

* Total AUM
* SIP Inflows
* Folios
* Number of Schemes
* AUM Trends
* Fund House Analysis

## Page 2 — Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* NAV vs Benchmark
* Performance Filters

## Page 3 — Investor Analytics

* State-wise Transactions
* Investment Mode Distribution
* Age Group Analysis
* Monthly Transaction Trends

## Page 4 — SIP & Market Trends

* SIP vs NIFTY Analysis
* Category Inflows
* SIP Growth Metrics
* Market Trend Monitoring

---

# Key Findings

1. Mutual fund industry AUM demonstrated strong long-term growth.
2. SIP inflows reached record highs during the analysis period.
3. Small-cap funds delivered higher returns but carried greater downside risk.
4. Investor participation increased significantly through SIP investments.
5. Several funds exhibited strong risk-adjusted performance based on Sharpe Ratio.
6. Portfolio concentration varied considerably across schemes.
7. Most investors showed irregular SIP contribution patterns based on continuity analysis.

---

# Folder Structure

```text
data/
raw/
processed/

notebooks/
Day1_Data_Ingestion.ipynb
Day2_Data_Cleaning.ipynb
EDA_Analysis.ipynb
Performance_Analytics.ipynb
Advanced_Analytics.ipynb

src/
data_ingestion.py
live_nav_fetch.py
create_database.py
recommender.py
run_pipeline.py

sql/
schema.sql
queries.sql

dashboard/
bluestock_mf_dashboard.pbix

reports/
charts/
screenshots/
Final_Report.pdf
```

# Setup Instructions

Clone Repository

```bash
git clone <repository-url>
```

Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy sqlalchemy
```

---

# How to Run

Run ETL Pipeline

```bash
python src/run_pipeline.py
```

Run Notebook Analysis

Open Jupyter Notebook and execute:

* EDA_Analysis.ipynb
* Performance_Analytics.ipynb
* Advanced_Analytics.ipynb

Open Dashboard

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

# Future Improvements

* Live AMFI API integration
* Machine Learning based recommendations
* Portfolio optimization engine
* Predictive SIP forecasting
* Investor churn prediction
* Cloud deployment on AWS

---

# Author

Ekta Rajak

MBA | Data Analytics Enthusiast

Skills: Python, SQL, Power BI, Statistics, AWS, Data Visualization
