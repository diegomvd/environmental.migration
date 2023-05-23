import pandas as pd

mig_data = pd.read_csv("./data/mig_total_outflow_per_country.csv").drop(columns="Unnamed: 0")

pop_data = pd.read_csv("./data/population_data_five_year_average.csv").drop(columns="Unnamed: 0")

pop_data["country"] = pop_data.country.apply(lambda c: c.replace(" ",""))

data = pd.merge(left = mig_data, right = pop_data, how="inner", on=["country","year0"])

data["pct_outflow"] = data["flow"]/data["total"]*100.0

data = data.rename(
    {
        "flow" : "net_outflow",
        "pct_outflow" : "pct_outflow",
        "total" : "population",
        "rural" : "pct_rural",
        "urban" : "pct_urban"
    },
    axis="columns"
)
data = data[ ["year0", "country", "pct_outflow", "net_outflow", "population", "pct_rural", "pct_urban" ]  ]

data.to_csv("./data/mig_outflow_normalized.csv")
