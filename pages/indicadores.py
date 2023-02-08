import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
import dash_daq as daq
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
                        
                        dbc.Col([
                            dbc.Card(
                                style=CARD_STYLE,
                                className=CARD_CLASS,
                                children=[

                                    html.P(id='kpi-3-title', children=[]),
                                    html.H1(id='kpi-3', style={'align-self': 'center'}, children=[]),
                                    html.H6(id='kpi-3-rate', style={'align-self': 'end'}, children=[])
                                
                                ]
                            ),
                        ]),
                        
                        dbc.Col([
                            dbc.Card(
                                style=CARD_STYLE,
                                className=CARD_CLASS,
                                children=[

                                    html.P(id='kpi-4-title', children=[]),
                                    html.H1(id='kpi-4', style={'align-self': 'center'}, children=[]),
                                    html.H6(id='kpi-4-rate', style={'align-self': 'end'}, children=[])
                                
                                ]
                            ),
                        ]),
                        
                    ]
                ),

### Circular graphs ###
                dbc.Col(
                    className='col-3',
                    style={'margin-top': '20px'},
                    children=[

                        dbc.Row(
                            children=[
                                dbc.Card(
                                    className= CARD_CLASS,
                                    style=CARD_STYLE,
                                    children=[

                                        daq.Gauge(
                                            id='velocimeter',
                                            color={"gradient":True,"ranges":{"red":[0,40], "yellow":[40,70],"green":[70,100]}},
                                            value=80,
                                            label='Performance',
                                            max=100,
                                            min=0,
                                        )

                                    ]
                                ),
                            ]
                        ),
                            
                        dbc.Row(
                            children=[
                                dbc.Card(
                                    className= CARD_CLASS,
                                    id='rolette',
                                    children=['foo']
                                ),
                            ]
                        ),

                ]),

### CHARTS ###
                dbc.Col(
                    className='col-9',
                    style={'margin-top': '20px'},
                    children=[
                        
                        dbc.Row(
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
                            
                        dbc.Row([

                            dbc.Col(
                                className='col-6',
                                children=[
                                    dbc.Card(
                                        id='minigraph-1',
                                        className= CARD_CLASS,
                                        children=['foo']
                                    ),
                                ]
                            ),
                            
                            dbc.Col(
                                className='col-6',
                                children=[
                                    dbc.Card(
                                        id='minigraph-2',
                                        className= CARD_CLASS,
                                        children=['foo']
                                    ),
                                ]
                            ),

                        ])
                        

                ])


            ]
        )
    
    ]
)