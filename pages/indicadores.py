import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
import dash_daq as daq
# import dash_bootstrap_components as dbc
import pandas as pd

from static.styles import *

dre_fields = pd.read_csv('assets/dre_2021.csv')['conta'].values
print(dre_fields)

CARD_STYLE = {'padding': '10px', 'margin': '10px', 'border': 'None', **FONT_STYLE}
CARD_CLASS = 'shadow-sm rounded-0'
ROW_CLASS = 'g-0'

indicadores = dbc.Row(
    children=[
        
        dbc.Container(
            class_name='row',
            # style={'margin-top': '20px', 'width': '100%'},
            children = [

### FILTERS ###
                dbc.Row(
                    children=[
                        dcc.Dropdown(
                            className=CARD_CLASS , 
                            options=['2021', '2022'], 
                            value='2021', 
                            placeholder='ANO', 
                            id='indicador-ano-dropdown', 
                            style={"max-width": "200px", 'border': 'None', **FONT_STYLE}
                        ),
                        dcc.Dropdown(
                            className=CARD_CLASS , 
                            options=[
                                'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
                                'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
                            ], 
                            value='JAN',
                            placeholder='MES', 
                            id='indicador-mes-dropdown', 
                            style={"max-width": "200px", 'border': 'None', **FONT_STYLE}
                        ),
                    ]
                ),

###### Content #####

### KPIs ###
                dbc.Row(
                    className=ROW_CLASS,
                    children=[
                            dbc.Col([
                                dbc.Card(
                                    style=CARD_STYLE,
                                    className=CARD_CLASS,
                                    children=[
                                        html.P(id=f'kpi-{i}-title', children=[], style=FONT_STYLE),
                                        html.H1(id=f'kpi-{i}', style={'align-self': 'center', **FONT_STYLE}, children=[]),
                                        html.H6(id=f'kpi-{i}-rate', style={'align-self': 'end', **FONT_STYLE}, children=[])
                                    ]
                                ),
                            ])
                            for i in range(1,5)
                    ]
                ),

### Circular graphs ###
                dbc.Col(
                    className='col-3',
                    children=[

                        dbc.Row(
                            children=[
                                dbc.Card(
                                    className= CARD_CLASS,
                                    style=CARD_STYLE,
                                    children=[
                                        html.H6('Performance', style=FONT_STYLE),
                                        daq.Gauge(
                                            id='velocimeter',
                                            color={"gradient":True,"ranges":{"red":[0,40], "yellow":[40,70],"green":[70,100]}},
                                            value=80,
                                            label=' ',
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
                                    className= f'{CARD_CLASS}',# align-items-center',
                                    style=CARD_STYLE,
                                    children=[
                                        
                                        dbc.Row([
                                            dbc.Col([ html.H6('Meta ', style=FONT_STYLE) ]),
                                                dcc.Dropdown(
                                                    className=CARD_CLASS , 
                                                    options=dre_fields, 
                                                    value=dre_fields[0], 
                                                    placeholder='CONTA', 
                                                    id='progress-dropdown', 
                                                    style={"max-width": "300px", 'border': 'None', **FONT_STYLE}
                                                ),
                                        ]),
                                        dcc.Graph(id='progress-chart')

                                    ]
                                ),
                            ]
                        ),

                ]),

### CHARTS ###
                dbc.Col(
                    className='col-9',
                    children=[
                        
                        dbc.Row(
                            className=ROW_CLASS,
                            children=[
                                dbc.Card(
                                    className=CARD_CLASS,
                                    style={**CARD_STYLE, "padding": "16px"},
                                    children=[
                                        
                                        html.H5(id='main-chart-title', style=FONT_STYLE),
                                        dcc.Graph(
                                            id='main-chart',
                                            # style={'max-height': '300px'}
                                        )

                                    ]
                                ),

                            ]
                        ),                        
                            
                        dbc.Row(
                            className=ROW_CLASS,
                            children=[

                                dbc.Col(
                                    className='col-6',
                                    children=[
                                        dbc.Card(
                                            className= CARD_CLASS,
                                            style= {'max-height': '280px', **CARD_STYLE},
                                            children=[
                                                html.H6(id=f'minigraph-{i}-title', style=FONT_STYLE),
                                                dcc.Graph(
                                                    # className='four columns', 
                                                    id=f'minigraph-{i}',
                                                    style={'max-height': '249px'},
                                                    config={'responsive': True}
                                                )

                                            ]
                                        ),
                                    ]
                                )
                                for i in range(1,3)

                            ]
                        )

                ])

            ]
        )

    ]
)