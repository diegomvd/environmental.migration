import pandas as pd

data = pd.read_csv("./data/mig_outflow_normalized.csv")

countries = [
    "MDV", "MLT", "VCT", "BRB", "ATG", "SYC", "LCA", "FSM", "TON", "DMA", "BHR", "KIR", "STP", "COM", "MUS", "WSM", "CPV", "TTO", "BRN", "CYP", "BHS", "VUT", "FJI", "SLB", "JAM", "GMB", "GMB", "MNE", "BLZ", "DJI",
]

data = data[data.country.isin(countries)]

data.to_csv("./data/mig_outflow_30_small_countries.csv")