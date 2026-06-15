import pandas as pd

fund_master = pd.read_csv(
    "../data/processed/clean_fund_master.csv"
)

sharpe = pd.read_csv(
    "../data/processed/sharpe_values.csv"
)

recommender_data = sharpe.merge(
    fund_master[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "risk_category"
        ]
    ],
    on="amfi_code",
    how="left"
)

def recommend_funds(risk_appetite):
    recommendations = (
        recommender_data[
            recommender_data["risk_category"] == risk_appetite
        ]
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_category",
            "sharpe_ratio"
        ]
    ]

print("\nLOW RISK\n")
print(recommend_funds("Low"))

print("\nMODERATE RISK\n")
print(recommend_funds("Moderate"))

print("\nHIGH RISK\n")
print(recommend_funds("High"))
