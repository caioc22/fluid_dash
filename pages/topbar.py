import dash_bootstrap_components as dbc
from dash import html, dcc

from static.styles import *

topbar = dbc.Row(
            className='d-flex shadow-sm align-items-center',
            style={
                'width': '100%', 
                'padding': '10px', 
            },
            children = [
                dbc.Col(
                    className='col-10',
                    children=[
                        html.H3(
                            id='page-title',
                            style={'font-family': 'DM sans', 'color': '#0d6efd'},
                        ),
                    ]
                ),
                dbc.Row(
                    className='col-2 align-items-center ',
                    style={'justify-content': 'flex-end'},
                    children=[
                        dbc.Col([ html.H6('Olá, Fulano!', style=FONT_STYLE) ]),
                        dbc.Col([ 

                            html.I(className="bi bi-person-circle", style={'font-size': '30px', 'color': STD_BLUE}) 
                        ]),
                    ]
                )
            ]
        )
