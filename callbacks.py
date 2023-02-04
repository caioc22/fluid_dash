import dash_bootstrap_components as dbc
from plotly import express as px, graph_objects as go
import pandas as pd, numpy as np, re

from index import *

from utils.kpis import *

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


### INDICADORES ####
@app.callback(
    Output('kpi-1', 'children'), Output('kpi-1-rate', 'children'),
    
    Input('url', 'pathname'), 
    Input('indicador-ano-dropdown', 'value'),
    Input('indicador-mes-dropdown', 'value'),
    Input('kpi-1-dropdown', 'value'),
)
def update_kpis(url, ano, mes, kpi1):
    meses = [
        'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
        'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
    ]
    
    if url == '/indicadores':
        conta = 'LUCRO BRUTO'

        data = pd.read_csv(f'assets/dre_{ano}.csv', index_col=[0])
        
        current_value = data.loc[data['conta'].str.contains(conta)][mes].values[0]
        
        mes_idx = meses.index(mes)
        last_mes = meses[mes_idx-1] if mes_idx != 1 else 11
        last_value = data.loc[data['conta'].str.contains(conta)][last_mes].values[0]
        
        rate = round(((current_value/last_value)-1)*100 , 2)

        return current_value, f'{rate}%'
        

@app.callback(
    Output('main-chart', 'figure'), Output('main-chart-title', 'children'),
    
    Input('url', 'pathname'), 
    Input('indicador-ano-dropdown', 'value'),
    Input('indicador-mes-dropdown', 'value'),
    Input('kpi-1-dropdown', 'value'),
)
def update_main_chart(url, ano, mes, chart):
    meses = [
        'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
        'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
    ]
    
    if url == '/indicadores':
        conta = 'LUCRO BRUTO'

        data = pd.read_csv(f'assets/dre_{ano}.csv', index_col=[0])
        
        plot = data.loc[data['conta'].str.contains('LUCRO BRUTO')][meses].T

        fig = go.Figure(
            data=go.Scatter(
                x=plot.index, 
                y=plot.iloc[:, 0], 
                mode='lines')
            )

        fig.update_layout( 
                margin=dict(t=0, l=0, r=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
            )
        
        return fig, conta