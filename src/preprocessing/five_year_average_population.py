import pandas as pd
import numpy as np

data = pd.read_csv("./data/population_per_country.csv")

# Convert the per 1000 data to the actual number.
data["Value"] = data["Value"]*1000.0

data = data.drop(columns=["Domain","Unit","Item"])

data = data.rename(
    {
        "Area" : "country",
        "Year" : "year",
        "Value" : "value",
        "Element": "element"
    },
    axis="columns"
)

data = data.pivot_table(index = ["country","year"], columns="element", values="value").reset_index()
data = data.rename(
    {
        "Total Population - Both sexes" : "total",
        "Rural population" : "rural",
        "Urban population" : "urban"
    },
    axis="columns"
)

df = pd.DataFrame()
for year0 in [1990,1995,2000,2005,2010,2015]:
    years = np.arange(year0,year0+6,1)
    grouped = data[data.year.isin(years)].groupby("country").mean().reset_index().drop(columns="year")
    grouped["year0"] = year0
    df = pd.concat([df,grouped],axis=0, ignore_index=True)  

data = df

data["rural"] = data["rural"]/data["total"]*100.0
data["urban"] = data["urban"]/data["total"]*100.0

country_codes = pd.read_csv("./data/countries_codes_and_coordinates.csv")

def get_country_code(codes, country):
    code = codes[codes.Country == country].reset_index()["Alpha-3 code"]
    try:
        ret = code[0]
    except:
        ret = "NONE"
    ret = ret.replace("\"", "")
    return ret

data["country_code"] = data.country.apply(lambda c: get_country_code(country_codes,c)) 

data = data.drop(columns="country").rename({"country_code":"country"},axis="columns")

data.to_csv("./data/population_data_five_year_average.csv")
