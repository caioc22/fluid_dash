import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

balanco = html.Div(
    style={'width': '100%'},
    children=[
    
        dbc.Container(
            className='row',
            style={'margin-top': '20px'},
            children = [
                    html.H3(
                        style={'font-family': 'Helvetica', 'color': '#0d6efd'},
                        children='Balanço Patrimonial'
                        ),
                    # adicionar label
                    dcc.Dropdown(
                        options=[
                            {'label': 'Semestral', 'value': 'sem'},
                            {'label': 'Anual', 'value': 'year'}
                        ], 
                        value='s1', 
                        id='balance-period-dropdown', 
                        style={"max-width": "200px"}
                    ),
        ]),

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
                html.Div(id='table-tile'),
                dash_table.DataTable(
                    id='balance-table',
                    row_selectable='single',
                    page_size=10,
                    page_action='none',
                    style_table={'height': '400px', 'overflowY': 'auto', 'width': '80%'}
                )
            ]
        )

])



