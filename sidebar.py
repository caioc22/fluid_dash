from dash import html
import dash_bootstrap_components as dbc

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "12rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
# blue => #1284C3
# shalow-gray => #f8f9fa

# the styles for the main content position it to the right of the sidebar and
# add some padding.


sidebar = html.Div(
    [
        html.H2("Dashboard", className="display-4", style={'font-size': '30px'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    className="row",
                    children=[
                        html.I(className="bi bi-house-door-fill"),
                        "Home"
                    ], 
                    href="/", 
                    active="exact"),

                dbc.NavLink(
                    className="row",
                    children=[
                        html.I(className="bi bi-bar-chart"),
                        "Indicadores"
                    ], 
                    href="/indicadores", 
                    active="exact"),
                    
                dbc.NavLink(
                    className="row",
                    children=[
                        html.I(className="bi bi-clipboard-data"),
                        "Balanço"
                    ], 
                    href="/balanco", 
                    active="exact"),
                    
                dbc.NavLink(
                    className="row",
                    children=[
                        html.I(className="bi bi-graph-up"),
                        "DRE"
                    ], 
                    href="/dre", 
                    active="exact"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


