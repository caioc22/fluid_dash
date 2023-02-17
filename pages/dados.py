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
                    className='col-3',
                    children=[

                        dbc.Card(
                            style={ 
                                'padding': '8px',
                                'height': '80%',
                                'vertical-align': 'text-top',
                                **CARD_STYLE
                                },
                            className = 'shadow-sm',
                            children=[
                                html.H6('Upload', style=FONT_STYLE),
                            ]
                        )

                    ]
                ),
                
                dbc.Col(
                    className='col-3',
                    children=[

                        dbc.Card(
                            style={ 
                                'padding': '8px',
                                'height': '80%',
                                'vertical-align': 'text-top',
                                **CARD_STYLE
                                },
                            className = 'shadow-sm justify-content-center',
                            children=[
                                html.H6('Download', style=FONT_STYLE),
                            ]
                        )

                    ]
                )

            ]
        )
        
    ]
)