import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv('/assets/dre_random.csv', index_col=[0])
df = df.drop(columns=['tipo', 'nivel'])
data = df[['conta', 'JUL', 'AGO', 'OUT', 'NOV', 'DEZ']]

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

dre = html.Div(
    style=CONTENT_STYLE,
    
    children=[
    
        html.Div([
            dbc.Row(
                children=[
                    html.H1(children='Demonstração de Resultados de Exercício 2022'),
                    dcc.Dropdown(
                        options=['2021', '2022'], 
                        value='2022', 
                        id='period-dropdown', 
                        style={"max-width": "200px"}
                    )
                ]
            ),
        ]),

        # dcc.Loading(
        #     children=[
        #         html.Div(id='dre-charts', className='row', children=[])
        #     ]
        # )

        html.Div(
            id='dre-chart',
            style={'margin-top': '20px'},
            children=[

                dbc.Row(
                    id='dre-charts'
                )

                # dbc.Row(
                #     children=[
                        
                        # dbc.Col(
                        #     children=[
                        #         dbc.Card([

                        #             dbc.CardBody([
                        #                 html.H4('Body')
                        #             ])
                        #         ])
                        #     ]
                        # ),
                        
                        # dbc.Col(
                        #     children=[
                        #         dbc.Card([

                        #             dbc.CardBody([
                        #                 html.H4('Body')
                        #             ])
                        #         ])
                        #     ]
                        # ),
                        
                        # dbc.Col(
                        #     children=[
                        #         dbc.Card([

                        #             dbc.CardBody([
                        #                 html.H4('Body')
                        #             ])
                        #         ])
                        #     ]
                        # )
                    
                #     ]
                # )

            ]
        )

        
        # dcc.Graph(
        #     id='bar-chart', 
        # ),

        # dash_table.DataTable(
        #     data=data.to_dict('records'), 
        #     columns=[{"name": i, "id": i} for i in df.columns],
        #     page_size=10
        # )
])



