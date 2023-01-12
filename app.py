from dash import Dash, dash_table, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from sidebar import sidebar
from plotly import express as px, graph_objects as go
from dre import dre, data
import pandas as pd, numpy as np

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

CONTENT_STYLE = {
    "margin-left": "14rem",
    "width": "100%"
}


app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    sidebar, 
    html.Div(
        style=CONTENT_STYLE,
        id='page-content'
        )
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
    elif pathname == "/indicadores":
        return 'Indicadores'
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
        columns = []
        
        for field, op, c in zip( data['conta'], data['tipo'], range(len(data['conta'])) ):
            
            reversed = {}
            color = 'rgba(50, 171, 96, 0.6)'
            line_color = 'rgba(50, 171, 96, 1.0)'
            if op == '-':
                color = 'rgba(245, 39, 39, 0.6)'
                line_color = 'rgba(245, 39, 39, 1.0)'
                reversed = {'yaxis': {'autorange': 'reversed'}}
            
            print(field, 'counter', c+1)
            print(data.columns)
            y = data.loc[data['conta'] == field].iloc[:, 1:]
            y.drop(columns=['tipo', 'nivel'], inplace=True)
            print(y.columns)
            y = y.T.iloc[:, 0]
            print(y)

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=y.index.values,
                    y=y,
                    marker={'color': '#f43b47'},
                    showlegend=False
                ))

            fig.add_trace(
                go.Bar(
                    x=y.index.values,
                    y=y,
                    marker={
                        'line': {
                            'width':1,
                            'color': line_color,
                            },
                        'color': color
                    },
                    showlegend=False
                ))
            
            fig.update_layout( 
                margin=dict(t=0, l=0, r=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                **reversed
            )

            columns.append(
                    dbc.Card(
                        style={ 'width': '28%', 
                                'height': '250px', 
                                'margin-left': '10px', 
                                'margin-bottom': '20px', 
                                'padding': '8px',
                                'vertical-align': 'text-top'
                                },
                        className = 'shadow-sm',
                        children=[
                            html.H6(field),
                            dcc.Graph(
                                # className='four columns', 
                                style={'max-height': '249px'} ,
                                figure=fig
                            ),
                    ])
                )
            
            # if (c+1) == 6:
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

    print('nao foi')
    return []

app.name = 'Dashboard'


if __name__ == '__main__':
    app.run_server(port=8001)#, debug=False)