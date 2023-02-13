# https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
from dash import html
import dash_bootstrap_components as dbc

from static.styles import *

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#1284C3",
    # "background-color": "#f8f9fa",
    # "background": "linear-gradient(135deg, rgba(18,131,195,1) 0%, rgba(18,131,195,1) 34%, rgba(255,255,255,0) 100%)"
}
NAV_LINK_STYLE = "row link-light"
RESIZE_LOGO = 30

sidebar = html.Div(
    style=SIDEBAR_STYLE,
    children=[
        html.Div(
            className="row align-items-center link-light",
            style={"font-size": "25px", **FONT_STYLE},
            children=[
                html.Img(src="assets/fluid_white.png", style={"height": f"{RESIZE_LOGO}%", 
                                                              "width": f"{RESIZE_LOGO}%"}),
                # html.H2("Fluid.BI", className="row display-4", style={'font-size': '30px'}),
                "Fluid.BI"
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
                    href="/indicadores", 
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


