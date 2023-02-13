import dash_bootstrap_components as dbc
from dash import html, dcc

topbar = dbc.Row(
            className='d-flex shadow-sm',
            style={
                'margin-top': '20px', 
                'width': '100%', 
                'padding': '10px', 
                'justify-content': 'between'
            },
            children = [
                dbc.Col([
                    html.H3(
                        id='page-title',
                        style={'font-family': 'DM sans', 'color': '#0d6efd'},
                    ),
                ]),
                dbc.Col([
                    html.I(className="bi bi-person-circle", style={'font-size': '24px'}),
                ])
            ]
        )
