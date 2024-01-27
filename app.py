from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

app = Dash(__name__)

fig = px.line(
    df,
    x='time',
    y='duration',
    title='Duration over time',
    color='testcase',
    markers=True
)

fig.add_vline(x='2024-01-26 14:00:00')

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)