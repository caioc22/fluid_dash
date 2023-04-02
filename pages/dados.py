import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

from static.styles import *

dados = dbc.Row(
    className='align-items-center',
    children=[

        dbc.Container(
            className='row',
            children=[

                dbc.Col(
                    className='col-4',
                    children=[

                        dbc.Card(
                            style={ 
                                'padding': '8px',
                                'vertical-align': 'text-top',
                                **CARD_STYLE
                                },
                            className='shadow-sm',
                            children=[
                                html.H5('Upload', style={'width': '80%', **FONT_STYLE}),
                                html.P('Faça o upload de um documento:', style={'width': '80%', **FONT_STYLE}),
                                
                                html.Div([
                                    # dbc.Col([
                                    #     dcc.Dropdown(
                                    #         id='kind-data-dropdwon',
                                    #         className=CARD_CLASS,
                                    #         style=FONT_STYLE,
                                    #         options=['DRE', 'Balanço Patrimonial', 'Balancete', 'Fluxo de Caixa'],
                                    #         placeholder='Tipo'
                                    #     ),
                                    # ], className='col-9'),
                                    dbc.Col([
                                        html.Button(
                                            className='btn btn-outline-secondary align-items-center',
                                            style={'width': '100%'},
                                            children=[
                                                dcc.Upload(
                                                    id='uploaded-file',
                                                    children=[ html.I(className='bi bi-upload') ],
                                                    multiple=False,
                                                )
                                            ]
                                        )
                                    ], style={'padding-left': 20, 'padding-right': 20,})#, className='col-3')
                                ], className='row'),

                                html.Div(
                                    id='uploaded-file-div', 
                                    className='align-items-center justify-content-center', 
                                    style={'width': '90%', **FONT_STYLE}
                                ),
                                
                            ]
                        ),
                        dbc.Card(
                            style={ 
                                'padding': '8px',
                                'vertical-align': 'text-top',
                                **CARD_STYLE,
                                },
                            className = 'shadow-sm justify-content-center',
                            children=[
                                html.Div([
                                    dbc.Col([ 
                                        html.H5('Dados Salvos', style={'width': '80%', **FONT_STYLE}) 
                                    ], className='col-8'),
                                    dbc.Col([ 
                                        dcc.Dropdown(
                                            id='dados-year-dropdown',
                                            options=[2021, 2022],
                                            placeholder='ANO'
                                        )
                                    ], className='col-4'), 
                                ], className='row', style={'margin-bottom': '10px', **FONT_STYLE}),
                                
                                dash_table.DataTable(
                                    id='saved-data-table',
                                    row_selectable='single',
                                    page_size=10,
                                    page_action='none',
                                    # fixed_rows={'headers': True},
                                    # style_header = {'display': 'none'},
                                    style_table={
                                        'max-height': '500px', 
                                        'overflowY': 'auto', 
                                        'width': '100%', 
                                        'justify-content': 'center'
                                    },
                                    style_cell={**FONT_STYLE},
                                    style_cell_conditional=[
                                        {
                                            'if': {'column_id': 'Nome'},
                                            'textAlign': 'left'
                                        }
                                    ],
                                    style_as_list_view=True,
                                )
                            ]
                        )

                    ]
                ),
                
                dbc.Col(
                    className='col-8',
                    children=[

                        dbc.Card(
                            style={ 
                                'padding': '8px',
                                'vertical-align': 'text-top',
                                **CARD_STYLE
                                },
                            className = 'shadow-sm justify-content-center',
                            children=[

                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className='col-9',
                                            children=[ 
                                                html.H5(id='data-table-title', style=FONT_STYLE) 
                                            ]
                                        ),
                                        dbc.Row([
                                            dbc.Col([ 
                                                html.Button(
                                                    id='save-table', 
                                                    style=FONT_STYLE, 
                                                    className='btn btn-outline-warning',
                                                    children=['Renomear']) 
                                            ]),
                                            dbc.Col([ 
                                                html.Button(
                                                    id='save-table', 
                                                    style=FONT_STYLE, 
                                                    className='btn btn-outline-danger',
                                                    children=['Deletar']) 
                                            ]),
                                        ], className='col-3',)

                                    ]
                                ),

                                dbc.CardBody([
                                    dcc.Loading([
                                        dash_table.DataTable(
                                            id='data-table',
                                            page_action='none',
                                            # fixed_rows={'headers': True},
                                            style_table={
                                                'max-height': '900px', 
                                                'overflowY': 'auto', 
                                                'width': '100%'
                                            },
                                            style_cell={**FONT_STYLE},
                                            style_cell_conditional=[
                                                {
                                                    'if': {'column_id': 'conta'},
                                                    'textAlign': 'left'
                                                }
                                            ]
                                        )
                                    ]),
                                ]),
                                
                            ]
                        )

                    ]
                ),

                dcc.Store(id='file-uploaded'),
                dcc.Input(id='file-uploaded-name', type='hidden', value=''),

            ]
        )
        
    ]
)