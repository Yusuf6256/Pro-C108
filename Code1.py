import csv
import plotly.figure_factory as pf
import pandas as pd

df = pd.read_csv("data.csv")
fig = pf.create_distplot([df["Avg Rating"].tolist()],["Average Rating"],show_hist=False)
fig.show()