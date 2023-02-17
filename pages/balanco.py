import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

from static.styles import *

balanco = dbc.Row(
    children=[

    dbc.Container(
        class_name='row',
        children=[
    
    # dbc.Container(
    #     children = [

### FILTERS ###
        dbc.Col(
            children=[
                
            
        dbc.Row(
            children=[
                html.H6('Filtro', style=FONT_STYLE),
                dcc.Dropdown(
                    options=[
                        {'label': 'Semestral', 'value': 'sem'},
                        {'label': 'Anual', 'value': 'year'}
                    ], 
                    value='s1', 
                    id='balance-period-dropdown', 
                    style={"max-width": "200px"}
                ),
            ]
        ),

        # dcc.Loading(
        #     children=[
        #         html.Div(id='dre-charts', className='row', children=[])
        #     ]
        # )

### CHART ###
        dbc.Row(
            style={'margin-top': '20px'},
            children=[
                dbc.Row(
                    style={'width': '100%'},
                    children=[
                        
                        dbc.Card(
                            style={ 'width': '80%', 
                                    'height': '350px', 
                            #         'margin-left': '10px', 
                            #         'margin-bottom': '20px', 
                                    'padding': '8px',
                                    'vertical-align': 'text-top',
                                    **CARD_STYLE
                                    },
                            className = 'shadow-sm',
                            children=[
                                html.H6(id='balance-chart-title', style=FONT_STYLE),
                                dcc.Graph(
                                    id='balance-chart',
                                    style={'max-height': '349px'}
                                ),
                            ]
                        )

                    ]
                )
            ]
        ),

### TABLE ###
        dbc.Row(
            style={'margin-top': '20px'},
            children=[
                
                html.H6(id='selected-period-title', children=[], style=FONT_STYLE),
                dash_table.DataTable(
                    id='balance-table',
                    row_selectable='single',
                    page_size=10,
                    page_action='none',
                    # fixed_rows={'headers': True},
                    style_table={'height': '350px', 'overflowY': 'auto', 'width': '80%'},
                    style_cell={**FONT_STYLE},
                    style_cell_conditional=[
                        {
                            'if': {'column_id': 'conta'},
                            'textAlign': 'left'
                        }
                    ]

                )
            ]
        )

        ]
    )
    # ])
    ])

])

