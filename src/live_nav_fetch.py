import requests
import pandas as pd

# Scheme codes provided in project

schemes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_data = data["data"]

        df = pd.DataFrame(nav_data)

        file_name = f"../data/raw/{scheme_name}_live_nav.csv"

        df.to_csv(file_name, index=False)

        print(f"{scheme_name} saved successfully")

    else:

        print(f"Error fetching {scheme_name}")