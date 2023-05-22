import pandas as pd

data = pd.read_csv("./data/bilat_mig_sex_type.csv")

# Filter out return and transit estimates.
data = data[data.type == "outward"]

# Filter out estimates from demographic accounting methods.
data = data.drop(columns=["da_min_open","da_min_closed"])

# Aggregate migration estimates by sex and by destination, for each origin and each year. 
data = pd.DataFrame( 
        [ 
            { 
                "year0":y, 
                "country": o,
                "flow":data[(data.orig == o) & (data.year0 == y)]["da_pb_closed"].sum()
            } 
            for y in data.year0.unique() for o in data.orig.unique() 
        ] 
    )

data.to_csv("./data/mig_total_outflow_per_country.csv")