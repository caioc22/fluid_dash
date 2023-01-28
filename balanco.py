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
                    dcc.Dropdown(
                        options=[
                            {'label': 'Semestre 1', 'value': 's1'},
                            {'label': 'Semestre 2', 'value': 's2'}
                        ], 
                        value='s1', 
                        id='balance-semester-dropdown', 
                        style={"max-width": "200px"}
                    ),
                    dcc.Dropdown(
                        options=['2020', '2021', '2022'], 
                        value='s1', 
                        id='balance-year-dropdown', 
                        style={"max-width": "200px"}
                    )
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
                    id='balance-chart',
                    style={'width': '100%'}
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



