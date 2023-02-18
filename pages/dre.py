import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table#, Output, Input, State
# import dash_bootstrap_components as dbc
import pandas as pd

from static.styles import *

from .topbar import topbar

dre = dbc.Row(
    children=[
    
### FILTERS ###
        dcc.Dropdown(
            options=['2021', '2022'], 
            value='2022', 
            placeholder='ANO',
            id='dre-period-dropdown', 
            style={"max-width": "200px"}
        ),

        dbc.Container(
            className='row',
            style={'margin-top': '20px'},
            children=[

                dbc.Card(
                        style={ 'width': '30%', 
                                'height': '250px', 
                                'margin-left': '10px', 
                                'margin-bottom': '20px', 
                                'padding': '8px',
                                'vertical-align': 'text-top'
                                },
                        className = 'shadow-sm',
                        children=[
                            # dcc.Loading([
                                html.H6(id=f'dre-chart-{i}-title', style=FONT_STYLE),
                                dcc.Graph(
                                    id=f'dre-chart-{i}',
                                    style={'max-height': '249px'} ,
                                ),
                            # ])
                    ]
                )
                for i in range(1, 33)

            ]
        )

    ]
)



