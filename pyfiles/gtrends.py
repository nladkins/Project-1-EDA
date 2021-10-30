# %%
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
from datetime import datetime as dt

pyo.init_notebook_mode()

g2019 = pd.read_csv('data/loseweight2019.csv', names=['week', 'pop'], parse_dates=True)[2:]
g2020 = pd.read_csv('data/loseweight2020.csv', names=['week', 'pop'], parse_dates=True)[2:]

pd.to_datetime(g2019['week'])
pd.to_datetime(g2020['week'])

g2019['pop'] = g2019['pop'].astype('float')
g2020['pop'] = g2020['pop'].astype('float')

gdiff = g2020['pop'] - g2019['pop']
gdiff = gdiff.reset_index()
gdiff.columns = ['week', 'diff']
# %%
fig = px.bar(gdiff, gdiff['week'], gdiff['diff'])
pyo.plot(fig)
# %%

trace0 = go.Scatter(
        x=g2019['week'],
        y=g2019['pop']
)

trace1 = go.Scatter(
        x=g2020['week'],
        y=g2020['pop']
)

data = [trace0, trace1]

fig = px.line(data[0])
fig.add_trace(go.Scatter(x=g2020['week'], y=g2020['pop']))
pyo.plot(fig)

fig = go.Figure(
        data=g2019
)

fig.update_traces()
g2019['pop2'] = g2020['pop']
g2019.columns = ['week', '2019', '2020']

fig = px.line(g2019, x='week', y=g2019.columns[1])
fig.add_scatter(g2020, x='week', y=g2020.columns[1])
pyo.plot(fig, cliponaxis=True)

# %%
# fig = px.line()
# g2019.to_excel('diffs.xlsx')


df = pd.read_csv('data/comedgoogle.csv')
fig = px.line(df, x='week', y=df.columns[1:], template='plotly_dark')

fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x")

fig.write_html('interactive.html')
pyo.plot(fig)
