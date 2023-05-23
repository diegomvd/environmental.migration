import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Small islands

data = pd.read_csv("/home/dibepa/git/environmental.migration/data/processed/mig_outflow_30_small_countries.csv")

# Drop MNE for lack of data in initial years.
data = data.drop( data[data.country == "MNE"].index )

# (g.map(plt.axhline, y=0, color=".7", zorder=0,linewidth=2.5)
#   .map(plt.axvline, x=0, color=".7", zorder=0, linewidth=2.5)
#   .set_axis_labels("Change in urban population (percentual points)", "Outmigration change \n relative to population change")
#   .tight_layout(w_pad=0))

sns.set_style("darkgrid")

# # Outflow evolution
g= sns.relplot(data=data, x="year0", y="pct_outflow",kind="line")
g.fig.subplots_adjust(top=0.9)
g.set_axis_labels("Initial year", "Percentual outmigration flow")
plt.title("Average evolution of outmigration")
plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/average_trend_outmigration.png")

g=sns.relplot(data=data, x="year0", y="pct_outflow",hue="country",kind="line", height=6, aspect=1)
g.fig.subplots_adjust(top=0.9)
g.set_axis_labels("Initial year", "Percentual outmigration flow")
plt.title("Evolution of outmigration")
plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/trend_outmigration.png")

# # Urban area evolution
# g=sns.relplot(data=data, x="year0", y="pct_urban", kind="line")
# g.fig.subplots_adjust(top=0.9)
# plt.title("Evolution of urban population")
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/trend_urban.png")

# # # Population evolution
# g=sns.relplot(data=data, x="year0", y="population", kind="line")
# g.fig.subplots_adjust(top=0.9)
# plt.title("Evolution of popoulation size")
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/trend_population.png")

# Urban vs. outflow
# g = sns.relplot(data=data, col="year0", x="pct_rural", y="pct_outflow", hue="population", kind="scatter",height=4,aspect=1,col_wrap=3,s=100)
# (g.set_axis_labels("Percentage of rural population", "Percentual outmigration flow")
#   .set_titles("Initial year: {col_name}")
#   .tight_layout(w_pad=0.2))
# g.fig.subplots_adjust(top=0.9) 
# g.fig.suptitle('Outmigration vs. rurality')
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/outmigration_vs_rurality.png")


# Top outmigrating countries
# data_top = data.sort_values(by="pct_outflow",ascending=False).groupby("year0").head(5)
# g=sns.catplot(data=data_top, col="year0", x="country",y="pct_outflow", kind="bar",aspect=1,height=4,col_wrap=3)
# (g.set_axis_labels("Country", "Relative outmigration flow")
#   .set_titles("Initial year: {col_name}")
#   .tight_layout(w_pad=0))
# g.fig.subplots_adjust(top=0.9) # adjust the Figure in rp
# g.fig.suptitle('Top 5 countries')
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/larger_outmigration.png")

# # Bottom outmigrating countries
# data_top = data.sort_values(by="pct_outflow",ascending=True).groupby("year0").head(5)
# g = sns.catplot(data=data_top, col="year0", x="country",y="pct_outflow", kind="bar",aspect=1,height=4,col_wrap=3)
# (g.set_axis_labels("Country", "Relative outmigration flow")
#   .set_titles("Initial year: {col_name}")
#   .tight_layout(w_pad=0))
# g.fig.subplots_adjust(top=0.9) # adjust the Figure in rp
# g.fig.suptitle('Bottom 5 countries')
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/smaller_outmigration.png")

# Changes
# outflow_change = pd.DataFrame([ 
#     {
#         "outflow_change" : (data[(data.year0 == 2015) & (data.country == c)].reset_index()["net_outflow"][0] - data   [(data.year0 == 1990)&(data.country == c)].reset_index()["net_outflow"][0])/data[(data.year0 == 1990)&(data.country == c)].reset_index()["net_outflow"][0]*100,
#         "country" : c
#     }
#     for c in data.country.unique() 
# ])

# urban_change = pd.DataFrame([ 
#     {
#         "urban_change" : (data[(data.year0 == 2015) & (data.country == c)].reset_index()["pct_urban"][0] - data   [(data.year0 == 1990)&(data.country == c)].reset_index()["pct_urban"][0]),
#         "country" : c
#     }
#     for c in data.country.unique() 
# ])

# pop_change = pd.DataFrame([ 
#     {
#         "pop_change" : ((data[(data.year0 == 2015) & (data.country == c)].reset_index()["population"][0] - data[(data.year0 == 1990)&(data.country == c)].reset_index()["population"][0]))/data[(data.year0 == 1990)&(data.country == c)].reset_index()["population"][0]*100,
#         "country" : c
#     }
#     for c in data.country.unique() 
# ])

# data_change = pd.merge(left = outflow_change, right = urban_change, how="inner", on=["country"])
# data_change = pd.merge(left = data_change, right = pop_change, how="inner", on=["country"])

# data_change["relative_outflow_change"] = data_change["outflow_change"]/data_change["pop_change"]

# # Biggest change
# data_top = data_change.sort_values(by="outflow_change",ascending=False).head(10)
# g = sns.catplot(data=data_top, x="country", y="outflow_change", kind="bar")
# (g.set_axis_labels("Country", "Percentual outmigration change")
#   .tight_layout(w_pad=0))
# plt.title("Top 10 countries")
# plt.tight_layout()
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/top_outmigration_changes.png")

# data_top = data_change.sort_values(by="outflow_change",ascending=True).head(10)
# sns.catplot(data=data_top, x="country", y="outflow_change", kind="bar")
# (g.set_axis_labels("Country", "Percentual outmigration change")
#   .tight_layout(w_pad=0))
# plt.title("Bottom 10 countries")
# plt.tight_layout()
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/bottom_outmigration_changes.png")


# data_top = data_change.sort_values(by="relative_outflow_change",ascending=False).head(10)
# sns.catplot(data=data_top, x="country", y="relative_outflow_change", kind="bar")
# (g.set_axis_labels("Country", "Percentual outmigration change relative \nto population change")
#   .tight_layout(w_pad=0))
# plt.title("Top 10 countries")
# plt.tight_layout()
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/top_relative_outmigration_changes.png")


# data_top = data_change.sort_values(by="relative_outflow_change",ascending=True).head(10)
# sns.catplot(data=data_top, x="country", y="relative_outflow_change", kind="bar")
# (g.set_axis_labels("Country", "Percentual outmigration change relative\n to population change")
#   .tight_layout(w_pad=0))
# plt.title("Bottom 10 countries")
# plt.tight_layout()
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/bottom_relative_outmigration_changes.png")

# Relation with urban areas
# g = sns.relplot(data=data_change,x="urban_change",y="relative_outflow_change",color="coral",alpha=0.6,edgecolor="0.8",kind="scatter", s=100)
# (g.map(plt.axhline, y=0, color=".7", zorder=0,linewidth=2.5)
#   .map(plt.axvline, x=0, color=".7", zorder=0, linewidth=2.5)
#   .set_axis_labels("Change in urban population (percentual points)", "Outmigration change \n relative to population change")
#   .tight_layout(w_pad=0))
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/relative_outmigration_vs_urban_change.png")

# g = sns.relplot(data=data_change,x="urban_change",y="outflow_change",color="coral",alpha=0.6,edgecolor="0.8",kind="scatter", s=100)
# (g.map(plt.axhline, y=0, color=".7", zorder=0,linewidth=2.5)
#   .map(plt.axvline, x=0, color=".7", zorder=0, linewidth=2.5)
#   .set_axis_labels("Change in urban population (percentual points)", "Percentual outmigration change")
#   .tight_layout(w_pad=0))
# plt.savefig("/home/dibepa/git/environmental.migration/figures/small.states/outmigration_vs_urban_change.png")


plt.show()
# print(data)