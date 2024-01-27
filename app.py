from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Histogram'),
    dcc.Dropdown(df.testcase.unique(), 'mes', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.testcase==value]
    return px.line(dff, x='time', y='duration')

if __name__ == '__main__':
    app.run(debug=True)