import pandas as pd

# Read World Bank population file.
# skiprows=4 skips the metadata rows at the top.
df = pd.read_csv("data/country_population.csv", skiprows=4)

# Keep only the fields needed for this visualisation.
clean = df[
    [
        "Country Name",
        "Country Code",
        "2020",
        "2021",
        "2022",
        "2023",
        "2024"
    ]
].copy()

# Rename columns into simpler names for Vega-Lite.
clean = clean.rename(
    columns={
        "Country Name": "country_name_worldbank",
        "Country Code": "country",
        "2020": "population_2020",
        "2021": "population_2021",
        "2022": "population_2022",
        "2023": "population_2023",
        "2024": "population_2024"
    }
)

# Save clean file.
clean.to_csv("data/country_population_clean.csv", index=False)

print("Created data/country_population_clean.csv")