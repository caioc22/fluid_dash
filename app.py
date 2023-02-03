from dash import Dash, dash_table, html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
from views.sidebar import sidebar

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
app.name = 'Fluid.BI'

CONTENT_STYLE = {
    "margin-left": "14rem",
    "width": "100%",
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    sidebar, 
    html.Div(
        style=CONTENT_STYLE,
        id='page-content'
        )
])

from callbacks import *



if __name__ == '__main__':
    app.run_server(port=8001)#, debug=False)