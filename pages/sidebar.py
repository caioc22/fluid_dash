# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
from dash import html
import dash_bootstrap_components as dbc

from static.styles import *

# the style arguments for the sidebar. We use position:fixed and a fixed width

NAV_LINK_STYLE = "row link-light"
RESIZE_LOGO = 30

sidebar_full = html.Div(
    style=SIDEBAR_FULL_STYLE,
    children=[
        
        dbc.Row([
            dbc.Col([
                html.I(
                    id='toggle-sidebar', 
                    className='bi bi-chevron-left', 
                    style={'color': 'white'},
                    n_clicks=0, 
                ),
            ], className='col-3')# justify-content-end')
        ], className='justify-content-end'),

        html.Div(
            className="row align-items-center link-light",
            style={"font-size": "25px", **FONT_STYLE},
            children=[
                html.Img(
                    src="assets/fluid_white.png", 
                    style={"height": f"{RESIZE_LOGO}%", "width": f"{RESIZE_LOGO}%"}
                ),
                "Fluid BI"
        ]),
        html.Hr(style={'color': '#f8f9fa'}),
        dbc.Nav(
            children=[
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-bar-chart"),
                        "Indicadores"
                    ], 
                    href="/", 
                    active="exact"),
                    
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-clipboard-data"),
                        "Balanço"
                    ], 
                    href="/balanco", 
                    active="exact"),
                    
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-graph-up"),
                        "DRE"
                    ], 
                    href="/dre", 
                    active="exact"),
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,# list-group-flush mx-3 mt-4",
                    children=[
                        html.I(className="bi bi-stack"),
                        "Dados"
                    ], 
                    href="/dados", 
                    active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
)


toggled_sidebar = html.Div(
    style=SIDEBAR_TOGGLE_STYLE,
    children=[
        
        dbc.Row([
            dbc.Col([
                html.I(
                    id='toggle-sidebar', 
                    className='bi bi-chevron-left', 
                    style={'color': 'white'},
                    n_clicks=0, 
                ),
            ], className='col-3')# justify-content-end')
        ], className='justify-content-end'),

        html.Div(
            className="row align-items-center link-light",
            style={"font-size": "25px", **FONT_STYLE},
            children=[
                html.Img(
                    src="assets/fluid_white.png", 
                    style={"height": f"{RESIZE_LOGO}%", "width": f"{RESIZE_LOGO}%"}
                ),
                "Fluid BI"
        ]),
        html.Hr(style={'color': '#f8f9fa'}),
        dbc.Nav(
            children=[
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-bar-chart"),
                        "Indicadores"
                    ], 
                    href="/", 
                    active="exact"),
                    
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-clipboard-data"),
                        "Balanço"
                    ], 
                    href="/balanco", 
                    active="exact"),
                    
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,
                    children=[
                        html.I(className="bi bi-graph-up"),
                        "DRE"
                    ], 
                    href="/dre", 
                    active="exact"),
                dbc.NavLink(
                    style=FONT_STYLE,
                    className=NAV_LINK_STYLE,# list-group-flush mx-3 mt-4",
                    children=[
                        html.I(className="bi bi-stack"),
                        "Dados"
                    ], 
                    href="/dados", 
                    active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
)


