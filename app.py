from dash import Dash, dash_table, html, dcc, Output, Input, State
import sys
import dash_bootstrap_components as dbc

from pages.topbar import topbar
from pages.sidebar import sidebar_full

from static.styles import *

app = Dash(
    __name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP, 
        dbc.icons.BOOTSTRAP,
        'https://fonts.googleapis.com/css2?family=DM+Sans&display=swap',
    ],
    # meta_tags=[
    #     {
    #         "name": "viewport",
    #         "content": "width=device-width, initial-scale=1, maximum-scale=1",
    #     }
    # ],
)
# html.Link(href='/assets/custom.css', rel='stylesheet'),
app.title = 'Fluid.BI'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    dcc.Store(id='toggle-accumulator'),
    html.Div(id='sidebar', children=[sidebar_full]),

    html.Div(
        id='content-wrapper',
        # style=CONTENT_STYLE,
        children=[
            topbar,
            html.Div(
                id='page-content',
                style={
                    'padding-top': '10px', 
                    'padding-left': '20px', 
                    # 'padding-right': '0px'
                    }
            )
        ]
    )
])

from callbacks import *


if __name__ == '__main__':
    app.run_server(port=sys.argv[1], debug=False)#eval(sys.argv[2]) )