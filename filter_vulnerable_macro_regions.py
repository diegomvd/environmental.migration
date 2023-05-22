import pandas as pd

data = pd.read_csv("./data/mig_outflow_normalized.csv")

countries = [
    "ARG", "BRA", "URY", "CHL", "BOL", "PER", "ECU", "COL", "VEN", "GUY", "SUR", "PRY", "PAN", "CRI", "NIC", "HND", "GTM", "BLZ", "MEX", "SLV", 
    "MLI", "NER", "NGA", "MRT", "GIN", "SEN", "GMB", "GNB", "BFA", "SLE", "LBR", "CIV", "GHA", "TGO", "BEN",
    "ETH", "ERI", "DJI", "SOM", "SSD", "UGA", "KEN", "TZA", "RWA", "BDI",
    "PAK", "IND", "NPL", "BTN", "BGD",
    "PHL", "THA", "MYS", "VNM", "KHM", "IDN", "BRN", "PNG", "SGP", "LAO"
]

data = data[data.country.isin(countries)]

regions = {
    "Latin America" : ["ARG", "BRA", "URY", "CHL", "BOL", "PER", "ECU", "COL", "VEN", "GUY", "SUR", "PRY", "PAN", "CRI", "NIC", "HND", "GTM", "BLZ", "MEX", "SLV"],

    "West Africa" : ["MLI", "NER", "NGA", "MRT", "GIN", "SEN", "GMB", "GNB", "BFA", "SLE", "LBR", "CIV", "GHA", "TGO", "BEN"],
    
    "East Africa" : ["ETH", "ERI", "DJI", "SOM", "SSD", "UGA", "KEN", "TZA", "RWA", "BDI"],
    
    "South Asia" : ["PAK", "IND", "NPL", "BTN", "BGD"],
    
    "Southeast Asia" : ["PHL", "THA", "MYS", "VNM", "KHM", "IDN", "BRN", "PNG", "SGP", "LAO"]
}

def assign_region(regions,country):
    ret=""
    for region in regions:
        if country in regions[region]:
            ret = region
    return ret

data["region"] = data.country.apply(
        lambda c: assign_region(regions,c) 
    )

data = data.drop(columns="Unnamed: 0")

data.to_csv("./data/mig_outflow_vulnerable_macroregions.csv")