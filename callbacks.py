import dash_bootstrap_components as dbc
from plotly import express as px, graph_objects as go
import pandas as pd, numpy as np, re

from index import *

from utils.kpis import *


meses = [
    'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
]


### DRE ###
@app.callback(
    Output('dre-charts', 'children'),
    State('url', 'pathname'), Input('dre-period-dropdown', 'value')
)
def dre_add_charts(pathname, period):
    print(period)
    if pathname == "/dre":
        columns = []
        
        data = pd.read_csv(f'./assets/dre_{period}.csv', index_col=[0])

        for field, op, c in zip( data['conta'], data['tipo'], range(len(data['conta'])) ):
            
            reversed = {}
            color = 'rgba(50, 171, 96, 0.6)' # green
            line_color = 'rgba(50, 171, 96, 1.0)'
            if op == '-':
                color = 'rgba(245, 39, 39, 0.6)' # red
                line_color = 'rgba(245, 39, 39, 1.0)'
                reversed = {'yaxis': {'autorange': 'reversed'}}
            
            print(field, 'counter', c+1)
            y = data.loc[data['conta'] == field].iloc[:, 1:]
            y.drop(columns=['tipo'], inplace=True)
            y = y.T.iloc[:, 0]

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=y.index.values,
                    y=y,
                    marker={'color': '#f43b47'},
                    showlegend=False
                ))

            fig.add_trace(
                go.Bar(
                    x=y.index.values,
                    y=y,
                    marker={
                        'line': {
                            'width':1,
                            'color': line_color,
                            },
                        'color': color
                    },
                    showlegend=False
                ))
            
            fig.update_layout( 
                margin=dict(t=0, l=0, r=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                **reversed
            )

            columns.append(
                    dbc.Card(
                        style={ 'width': '28%', 
                                'height': '250px', 
                                'margin-left': '10px', 
                                'margin-bottom': '20px', 
                                'padding': '8px',
                                'vertical-align': 'text-top'
                                },
                        className = 'shadow-sm',
                        children=[
                            html.H6(field),
                            dcc.Graph(
                                # className='four columns', 
                                style={'max-height': '249px'} ,
                                figure=fig
                            ),
                    ])
                )
            
            # if (c+1) == 6:
        return columns

            # if (c+1) % 3 == 0:
            #     print('foi')
            #     rows.append(
            #         dbc.Row(
            #             children=[
            #                 columns
            #             ]
            #         )
            #     )
                
            #     columns = []
            #     return rows

    print('nao foi')
    return []


### BALANÇO ###
@app.callback(
    Output('balance-chart', 'figure'), Output('balance-chart-title', 'children'),
    Input('url', 'pathname'), 
    Input('balance-table', 'derived_virtual_selected_rows'),
    # Input('balance-period-dropdown', 'value'),
)
def update_balance_chart(url, idx):
    print('idx', idx)
    if idx == None:
        idx = []

    if url == '/balanco':
        print('======= balance_chart')
        
        # if interval == 'sem':
        periodos = ['s1_2020', 's2_2020', 's1_2021', 's2_2021', 's1_2022', 's2_2022']
        # elif interval == 'year':
        #     periodos = ['s1_2020', 's2_2020', 's1_2021', 's2_2021', 's1_2022', 's2_2022']

        y_plot = []; switch_color = []; switch_line_color = []
        for p in periodos:
            local_data = pd.read_csv(f'assets/balan_{p}.csv')
            
            if len(idx) == 0:
                field = 'A T I V O'
            else:
                field = local_data['nome_conta'].loc[idx[0]]
            
            y = local_data.loc[local_data['nome_conta'] == field]['saldo_atual'].values[0]
            y_plot.append(y)
            
            color = 'rgba(50, 171, 96, 0.6)' if y > 0 else 'rgba(245, 39, 39, 0.6)'
            switch_color.append(color)
            
            line_color = 'rgba(50, 171, 96, 1)' if y > 0 else 'rgba(245, 39, 39, 1)'
            switch_line_color.append(line_color)
            
            
        fig = go.Figure()
        green = 'rgba(50, 171, 96, 0.6)'
        line_color = 'rgba(50, 171, 96, 1.0)'

        fig.add_trace(
            go.Scatter(
                x=periodos,
                y=y_plot,
                marker={'color': '#FB9E0F'},
                showlegend=False
            )
        )

        fig.add_trace(
            go.Bar(
                x=periodos,
                y=y_plot,
                showlegend=False,
                # marker={
                #     'line': {
                #         'width':1,
                #         'color': line_color,
                #         },
                # },
            )
        )

        fig.update_traces(marker_color=switch_color, marker_line_color=switch_line_color)

        fig.update_layout( 
            margin=dict(t=0, l=0, r=0),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            barmode='stack'
        )

        return fig, field

    return {}


@app.callback(
    Output('balance-table', 'data'), Output('selected-period-title', 'children'),
    State('url', 'pathname'),
    Input('balance-chart', 'clickData')
)
def update_balance_table(url, click):
    print('called')
    label = click['points'][0]['label'] if click is not None else 's1_2020'
    if url == '/balanco':
        print('foi')
        balan_table = pd.read_csv(f'assets/balan_{label}.csv', index_col=[0])
        balan_table['saldo_atual'] = round(balan_table['saldo_atual'], 2)
        balan_table = balan_table[['nome_conta', 'saldo_ant', 'saldo_atual']]

        def horizontal_rate(x):
            if x['saldo_ant'] != 0:
                return round(((x['saldo_ant'] - x['saldo_atual']) / x['saldo_ant'] )*100, 2)
            return np.nan

        balan_table['%'] = balan_table.apply(horizontal_rate, axis=1)
        balan_table.columns = ['conta', 'saldo anterior', 'saldo atual', '%']
        return balan_table.to_dict('records'), f'Periodo: {label}' 

    return {}


##### INDICADORES #####
@app.callback(
    Output('kpi-1', 'children'), Output('kpi-1-rate', 'children'), Output('kpi-1-title', 'children'),
    Output('kpi-2', 'children'), Output('kpi-2-rate', 'children'), Output('kpi-2-title', 'children'),
    Output('kpi-3', 'children'), Output('kpi-3-rate', 'children'), Output('kpi-3-title', 'children'),
    Output('kpi-4', 'children'), Output('kpi-4-rate', 'children'), Output('kpi-4-title', 'children'),

    Input('url', 'pathname'), 
    Input('indicador-ano-dropdown', 'value'),
    Input('indicador-mes-dropdown', 'value'),
)
def update_kpis(url, ano, mes):
    
    if url == '/indicadores':
        metrics = {
            'LUCRO LIQUIDO': 'LIQUIDO', 
            'RECEITA BRUTA': 'BRUTA',
            'MARGEM LIQUIDA': ' ',
            'MARGEM BRUTA': ' '
            }

        values = []; rates = []; titles = [];
        for metric in metrics:
            data = pd.read_csv(f'assets/dre_{ano}.csv', index_col=[0])

            if metric == 'MARGEM LIQUIDA':
                luc_liq = data.loc[data['conta'].str.contains('LIQUIDO')][mes].values[0]
                rec_liq = data.loc[data['conta'].str.contains('LIQUIDA')][mes].values[0]
                margem_liq = round((luc_liq / rec_liq) * 100, 2)

                # referenciar ano passado
                last_mes = meses[mes_idx-1] if mes_idx != 1 else meses[-1]

                last_luc_liq = data.loc[data['conta'].str.contains('LIQUIDO')][last_mes].values[0]
                last_rec_liq = data.loc[data['conta'].str.contains('LIQUIDA')][last_mes].values[0]
                last_margem_liq = round((last_luc_liq / last_rec_liq) * 100, 2)
                rate = round(((margem_liq/last_margem_liq)-1)*100 , 2)

                titles.append(metric); values.append(margem_liq); rates.append(rate)

            elif metric == 'MARGEM BRUTA':
                rec_liq = data.loc[data['conta'].str.contains('LIQUIDA')][mes].values[0]
                rec_bru = data.loc[data['conta'].str.contains('BRUTA')][mes].values[0]
                margem_bru = round((rec_liq / rec_bru) * 100, 2)

                last_mes = meses[mes_idx-1] if mes_idx != 1 else meses[-1]

                last_rec_liq = data.loc[data['conta'].str.contains('LIQUIDA')][last_mes].values[0]
                last_rec_bru = data.loc[data['conta'].str.contains('BRUTA')][last_mes].values[0]
                last_margem_bru = round((last_rec_liq / last_rec_bru) * 100, 2)
                rate = round(((margem_bru/last_margem_bru)-1)*100 , 2)

                titles.append(metric); values.append(margem_bru); rates.append(rate)

            # Metricas do DRE (nao compostas)
            else:
                regex = metrics[metric]
                
                current_value = data.loc[data['conta'].str.contains(regex)][mes].values[0]
                
                mes_idx = meses.index(mes)
                last_mes = meses[mes_idx-1] if mes_idx != 1 else meses[-1]
                last_value = data.loc[data['conta'].str.contains(regex)][last_mes].values[0]
                
                rate = round(((current_value/last_value)-1)*100 , 2)
                
                titles.append(metric); values.append(current_value); rates.append(rate)

        return (
            values[0], f'{rates[0]}%', titles[0], 
            values[1], f'{rates[1]}%', titles[1],
            f'{values[2]}%', f'{rates[2]}%', titles[2],
            f'{values[3]}%', f'{rates[3]}%', titles[3],
        )
        

@app.callback(
    Output('main-chart', 'figure'), Output('main-chart-title', 'children'),
    
    Input('url', 'pathname'), 
    Input('indicador-ano-dropdown', 'value'),
    Input('indicador-mes-dropdown', 'value'),
)
def update_main_chart(url, ano, mes):
    
    if url == '/indicadores':
        regex = 'LIQUIDO'

        data = pd.read_csv(f'assets/dre_{ano}.csv', index_col=[0])
        
        plot = data.loc[data['conta'].str.contains(regex)][meses].T

        fig = go.Figure(
            data=go.Scatter(
                x=plot.index, 
                y=plot.iloc[:, 0], 
                mode='lines+markers',
                line=dict(color="#ffb700")
                ),
            )

        fig.update_layout( 
                margin=dict(t=8, l=0, r=0, b=5),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
            )
        
        titulo = 'LUCRO LIQUIDO'
        return fig, titulo


# @app.callback(
#     Output('velocimeter', 'figure'),
#     Input('url', 'pathname'), Input('indicador-ano-dropdown', 'value')
# )
def velocimeter(url, year):
    
    if url == '/indicadores':
        fig = go.Figure(
                go.Indicator(
                    mode = "gauge+number+delta",
                    value = 75,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Performance", 'font': {'size': 16}},
                    delta = {'reference': 70, 'increasing': {'color': "green"}},
                    gauge = {
                        'axis': {'range': [None, 100], 'tickwidth': 1},
                        'bar': {'color': "blue"},
                        'bgcolor': "white",
                        # 'borderwidth': 2,
                        # 'bordercolor': "gray",
                        'steps': [
                            {'range': [0, 30], 'color': 'red'},
                            {'range': [30, 70], 'color': 'yellow'},
                            {'range': [70, 100], 'color': 'green'}
                            ],
                        'threshold': {
                            'line': {'color': "cyan", 'width': 4},
                            'thickness': 0.75,
                            'value': 75
                            }
                        }
                    )
                )

        fig.update_layout(
            paper_bgcolor="lavender",
            font={'color': "darkblue", 'family': "Arial"}
            )

        return fig