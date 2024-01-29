from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime

df = pd.read_csv('requests.csv')
ev = pd.read_csv('events.csv')

df['dt'] = pd.to_datetime(df['dt'])
ev['dt'] = pd.to_datetime(ev['dt'])

app = Dash(__name__)

fig = px.histogram(
    df,
    x='dt',
    y='ms',
    title='Request duration',
    color="app",
    histfunc='avg',
)


for i, row in ev.iterrows():
    fig.add_vline(
        x=datetime.timestamp(row['dt']) * 1000,
        annotation_text=row['event'],
        annotation_position='top right',
        annotation_yshift=-(i%4) * 15,
    )

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)