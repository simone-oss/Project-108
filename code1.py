import pandas as pd 
import plotly.figure_factory as ff
df =pd.read_csv("data1.csv")
fig=ff.create_distplot ([df["Avg Rating"].tolist()],["rating"],show_hist=False)
fig.show()