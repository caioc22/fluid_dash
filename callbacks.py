# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
from dash import Output, Input, html
from plotly import express as px, graph_objects as go
from dre import data, dre
from app import app


@app.callback(
    Output('bar-chart', 'figure'), 
    Input('field-dropdown', 'value')
)
def change_field_bar(field):
    print(field)
    y = data.loc[data['conta'] == field].iloc[:, 1:].T.iloc[:, 0]
    print(y)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=y.index.values,
            y=y,
            marker={'color': '#f43b47'}
        ))

    fig.add_trace(
        go.Bar(
            x=y.index.values,
            y=y,
            marker={'color': '#0d6efd'}
        ))

    return fig