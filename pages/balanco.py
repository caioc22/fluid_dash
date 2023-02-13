import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

from static.styles import *

from .topbar import topbar

balanco = dbc.Row(
    style={'width': '100%'},
    children=[
    
### FILTERS ###
    dbc.Container(
        class_name='row',
        children = [

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

        html.Div(
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
                                    'vertical-align': 'text-top'
                                    },
                            className = 'shadow-sm',
                            children=[
                                html.H6(id='balance-chart-title'),
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

        html.Div(
            children=[
                html.Br(),
                # html.Div(id='table-tile'),
                html.H6(id='selected-period-title', children=[]),
                    
                    dash_table.DataTable(
                        id='balance-table',
                        row_selectable='single',
                        page_size=10,
                        page_action='none',
                        # fixed_rows={'headers': True},
                        style_table={'height': '350px', 'overflowY': 'auto', 'width': '80%'},
                        style_cell_conditional=[
                            {
                                'if': {'column_id': 'conta'},
                                'textAlign': 'left'
                            }
                        ]

                )
            ]
        )

    ])

])



