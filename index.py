from dash import Input, Output, State, html, dcc
from app import app

from pages.dre import dre
from pages.balanco import balanco
from pages.indicadores import indicadores
from pages.dados import dados
from pages.sidebar import *

from static import styles

#===> RENDER PAGES
@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname")
)
def render_page_content(pathname):
    print(pathname)

    if pathname == "/":
        return indicadores

    elif pathname == "/balanco":
        return balanco

    elif pathname == "/dre":
        return dre
    
    elif pathname == "/dados":
        return dados
        
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

# ===> render page title
@app.callback(
    Output('page-title', 'children'),
    Input('url', 'pathname')
)
def update_page_title(url):
    titles = {
        '/': 'Indicadores',
        '/balanco': 'Balanço Patrimonial',
        '/dre': 'Demonstração de Resultados de Exercício',
        '/dados': 'Dados',
        }
    
    title = titles[url]

    return title


# ===> Toggle Sidebar
@app.callback(
    Output('sidebar', 'children'), 
    Output('toggle-accumulator', 'value'), 
    Output('content-wrapper','style'),

    Input('toggle-sidebar', 'n_clicks'), Input('toggle-accumulator', 'value')
)
def toggle_sidebar(click, accumulator):
    accumulator = accumulator + click if accumulator is not None else 0
    print('toggle', accumulator)
    
    if accumulator % 2 == 0:
        print('toggled')
        styles.SIDEBAR_TOGGLE_STYLE['width'] = "5rem"
        CONTENT_STYLE = {"margin-left": "5rem"} 
        return toggled_sidebar, accumulator, CONTENT_STYLE

    styles.SIDEBAR_FULL_STYLE['width'] = "12rem"
    CONTENT_STYLE = {"margin-left": "12rem"} 
    return sidebar_full, accumulator, CONTENT_STYLE
    