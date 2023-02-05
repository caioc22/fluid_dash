import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

CARD_STYLE = {'padding': '6px'}
CARD_CLASS = 'shadow-sm rounded-0'

indicadores = html.Div(
    style={'width': '100%'},
    children=[

### FILTERS ###
        dbc.Row(
            children=[
                dcc.Dropdown(
                    options=['2021', '2022'], 
                    value='2021', 
                    id='indicador-ano-dropdown', 
                    style={"max-width": "200px"}
                ),
                dcc.Dropdown(
                    options=[
                        'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                        'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
                    ], 
                    value='JAN', 
                    id='indicador-mes-dropdown', 
                    style={"max-width": "200px"}
                ),
            ]
        ),

###### Content #####
        dbc.Container(
            class_name='row',
            style={'margin-top': '20px', 'width': '100%'},
            children = [
### KPIs ###
                dbc.Row(
                    children=[

                        dbc.Col([
                            dbc.Card(
                                style=CARD_STYLE,
                                className=CARD_CLASS,
                                children=[

                                    html.P(id='kpi-1-title', children=[]),
                                    html.H1(id='kpi-1', style={'align-self': 'center'}, children=[]),
                                    html.H6(id='kpi-1-rate', style={'align-self': 'end'}, children=[])
                                
                                ]
                            ),
                        ]),
                        
                        dbc.Col([
                            dbc.Card(
                                style=CARD_STYLE,
                                className=CARD_CLASS,
                                children=[

                                    html.P(id='kpi-2-title', children=[]),
                                    html.H1(id='kpi-2', style={'align-self': 'center'}, children=[]),
                                    html.H6(id='kpi-2-rate', style={'align-self': 'end'}, children=[])
                                
                                ]
                            ),
                        ]),
                        
                    ]
                ),

### Main Charts ###
                dbc.Row(
                    style={'margin-top': '20px'},
                    children=[

                        dbc.Col(
                            className='col-3',
                            children=[
                                dbc.Card(
                                    className= CARD_CLASS,
                                    id='velocimeter',
                                    children=['foo']
                                ),
                            ]
                        ),
                            
                        dbc.Col(
                            className='col-9',
                            children=[
                                dbc.Card(
                                    className=CARD_CLASS,
                                    style={"padding": "16px"},
                                    children=[
                                        
                                        html.H5(id='main-chart-title'),
                                        dcc.Graph(
                                            id='main-chart',
                                            # style={'max-height': '300px'}
                                        )

                                    ]
                                ),

                            ]
                        ),

                ]),

### FOOTER CHARTS ###
                dbc.Row(
                    style={'margin-top': '20px'},
                    children=[

                        dbc.Col(
                            className='col-2',
                            children=[
                                dbc.Card(
                                    id='kpi-5',
                                    children=['foo']
                                ),
                            ]
                        ),
                            
                        dbc.Col(
                            className='col-5',
                            children=[
                                dbc.Card(
                                    id='kpi-5',
                                    children=['foo']
                                ),
                            ]
                        ),
                        
                        dbc.Col(
                            className='col-5',
                            children=[
                                dbc.Card(
                                    id='kpi-5',
                                    children=['foo']
                                ),
                            ]
                        ),

                ])


            ]
        )
    
    ]
)