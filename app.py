from dash import Dash, dash_table, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from sidebar import sidebar
from plotly import express as px, graph_objects as go
from dre import dre, data
import pandas as pd, numpy as np

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    sidebar, 
    html.Div(id='page-content')
])

## RENDER PAGES
@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname")
)
def render_page_content(pathname):
    print(pathname)
    if pathname == "/":
        return "This is Home page!"
    elif pathname == "/balanco":
        return html.P("Balanco")
    elif pathname == "/dre":
        return dre
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(
    Output('dre-charts', 'children'),
    Input('url', 'pathname')
)
def add_charts(pathname):
    
    if pathname == "/dre":
        rows = []
        columns = []
        
        for field, c in zip( data['conta'], range(len(data['conta'])) ):
            print(field, 'counter', c+1)
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

            columns.append(
                    dbc.Col(
                        style={'width':     '33%'},
                        children=[
                            dbc.Card([

                                dbc.CardBody(
                                    children=[
                                        html.H6(field),
                                        dcc.Graph(
                                            className='four columns', 
                                            style={'max-height': '250px'} ,
                                            figure=fig
                                        ) 
                                ])
                            ])
                        ]
                    )
                )
            
            if c == 2:
                return columns
            # if (c+1) % 3 == 0:
            #     print('foi')
            #     rows.append(
            #         dbc.Row(
            #             children=[
            #                 columns
            #             ]
            #         )
            #     )
                
            #     columns = []
            #     return rows

        return rows

    print('nao foi')
    return []


if __name__ == '__main__':
    app.run_server(port=8001)#, debug=False)