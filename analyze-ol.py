import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

olinedf = pd.read_csv("2020-ol-success-metrics.csv")
WRxaxisline = 70.5
WRyaxisline = 60
PFFxaxisline = 65
PFFyaxisline = 67.5

olinedf['PBWRvar'] = olinedf['PBWR'] - WRyaxisline
olinedf['RBWRvar'] = olinedf['RBWR'] - WRxaxisline
olinedf['PBGrvar'] = olinedf['PFF-PB'] - PFFyaxisline
olinedf['RBGrvar'] = olinedf['PFF-RB'] - PFFxaxisline

fig = px.scatter(olinedf, x="RBWRd", y="PBWRd", title="Team Run Block Win Rate vs. Pass Block Win Rate", text="Tm")
fig.update_traces(textposition='top center')
fig.add_shape(type="line", x0=WRxaxisline, y0=44.75, x1=70.5, y1=75.25,line=dict(color="grey", dash="dot", width=2))
fig.add_shape(type="line", x0=66.5, y0=WRyaxisline, x1=74.5, y1=WRyaxisline,line=dict(color="grey", dash="dot", width=2))
fig.show()

fig = px.scatter(olinedf, x="PFF-RB", y="PFF-PB", title="Team Run Block PFF Grade vs. Pass Block PFF Grade", text="Tm")
fig.update_traces(textposition='top center')
fig.add_shape(type="line", x0=PFFxaxisline, y0=49, x1=PFFxaxisline, y1=86,line=dict(color="grey", dash="dot", width=2))
fig.add_shape(type="line", x0=44, y0=PFFyaxisline, x1=84, y1=PFFyaxisline,line=dict(color="grey", dash="dot", width=2))
fig.show()

fig = px.scatter(olinedf, x="RBDiff", y="PBDiff", title="Win Rate vs. PFF Grade Differences", text="Tm")
fig.update_traces(textposition='top center')
fig.show()
