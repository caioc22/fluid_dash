from dash import Input, Output, State, html, dcc
from app import app

from pages.dre import dre
from pages.balanco import balanco
from pages.indicadores import indicadores
from pages.dados import dados

#===> RENDER PAGES
@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname")
)
def render_page_content(pathname):
    print(pathname)

    if pathname == "/":
        return "This is Home page!"

    elif pathname == "/indicadores":
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
        '/indicadores': 'Indicadores',
        '/balanco': 'Balanço Patrimonial',
        '/dre': 'Demonstração de Resultados de Exercício',
        '/dados': 'Dados',
        }
    
    title = titles[url]

    return title
