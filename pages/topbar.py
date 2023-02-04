import dash_bootstrap_components as dbc
from dash import html, dcc

topbar = dbc.Row(
            className='row shadow-sm',
            style={'margin-top': '20px', 'width': '100%', 'padding': '10px'},
            children = [
                html.H3(
                    id='page-title',
                    style={'font-family': 'Helvetica', 'color': '#0d6efd'},
                    ),
            ]
        )
