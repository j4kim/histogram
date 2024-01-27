from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from datetime import datetime

df = pd.read_csv('requests.csv')

df['dt'] = pd.to_datetime(df['dt'])

app = Dash(__name__)

fig = px.histogram(
    df,
    x='dt',
    y='ms',
    title='Request duration',
    color="app",
    histfunc='sum',
)

fig.add_vline(
    x=datetime.timestamp(pd.to_datetime('2024-01-26 14:00:00')) * 1000,
    # x=1706274000000,
    annotation_text='Action',
    annotation_position='top right'
)

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)