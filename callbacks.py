import dash_bootstrap_components as dbc
from plotly import express as px, graph_objects as go
import pandas as pd, numpy as np
import os, re

from index import *

from utils.kpis import *


meses = [
    'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN',
    'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ'
]


### DRE ###
def create_update_dre_chart_function(i):
    def update_dre_chart(pathname, period):

        if pathname == "/dre":
            data = pd.read_csv(f'./data/dre_{period}.csv', index_col=[0])

            field = data['conta'][i]
            op = data['tipo'][i]

            reversed = {}
            color = 'rgba(50, 171, 96, 0.6)' # green
            line_color = 'rgba(50, 171, 96, 1.0)'
            if op == '-':
                color = 'rgba(245, 39, 39, 0.6)' # red
                line_color = 'rgba(245, 39, 39, 1.0)'
                reversed = {'yaxis': {'autorange': 'reversed'}}
            
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

            return field, fig

    return update_dre_chart

for i in range(0, 32):
    app.callback(
        Output(f'dre-chart-{i+1}-title', 'children'),
        Output(f'dre-chart-{i+1}', 'figure'),

        State('url', 'pathname'), 
        Input('dre-period-dropdown', 'value'),
    )(create_update_dre_chart_function(i))



# # @app.callback(
# #     Output('dre-charts', 'children'),
# #     State('url', 'pathname'), Input('dre-period-dropdown', 'value')
# # )
# def update_dre_charts(pathname, period):
#     print(period)
#     if pathname == "/dre":
#         columns = []
        
#         data = pd.read_csv(f'./data/dre_{period}.csv', index_col=[0])

#         for field, op, c in zip( data['conta'], data['tipo'], range(len(data['conta'])) ):
            
#             reversed = {}
#             color = 'rgba(50, 171, 96, 0.6)' # green
#             line_color = 'rgba(50, 171, 96, 1.0)'
#             if op == '-':
#                 color = 'rgba(245, 39, 39, 0.6)' # red
#                 line_color = 'rgba(245, 39, 39, 1.0)'
#                 reversed = {'yaxis': {'autorange': 'reversed'}}
            
#             print(field, 'counter', c+1)
#             y = data.loc[data['conta'] == field].iloc[:, 1:]
#             y.drop(columns=['tipo'], inplace=True)
#             y = y.T.iloc[:, 0]

#             fig = go.Figure()

#             fig.add_trace(
#                 go.Scatter(
#                     x=y.index.values,
#                     y=y,
#                     marker={'color': '#f43b47'},
#                     showlegend=False
#                 ))

#             fig.add_trace(
#                 go.Bar(
#                     x=y.index.values,
#                     y=y,
#                     marker={
#                         'line': {
#                             'width':1,
#                             'color': line_color,
#                             },
#                         'color': color
#                     },
#                     showlegend=False
#                 ))
            
#             fig.update_layout( 
#                 margin=dict(t=0, l=0, r=0),
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 plot_bgcolor='rgba(0,0,0,0)',
#                 **reversed
#             )

#             columns.append(fig)
            
#             # if (c+1) == 6:
#         return columns

#             # if (c+1) % 3 == 0:
#             #     print('foi')
#             #     rows.append(
#             #         dbc.Row(
#             #             children=[
#             #                 columns
#             #             ]
#             #         )
#             #     )
                
#             #     columns = []
#             #     return rows

#     print('nao foi')
#     return []


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
            local_data = pd.read_csv(f'data/balan_{p}.csv')
            
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
        balan_table = pd.read_csv(f'data/balan_{label}.csv', index_col=[0])
        balan_table['saldo_atual'] = round(balan_table['saldo_atual'], 2)
        balan_table = balan_table[['nome_conta', 'saldo_ant', 'saldo_atual']]

        def horizontal_rate(x):
            if x['saldo_ant'] != 0:
                return round(((x['saldo_atual'] - x['saldo_ant']) / x['saldo_ant'] )*100, 2)
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
    
    if url == '/':
        metrics = {
            'LUCRO LIQUIDO': 'LIQUIDO', 
            'RECEITA BRUTA': 'BRUTA',
            'MARGEM LIQUIDA': ' ',
            'MARGEM BRUTA': ' '
            }

        values = []; rates = []; titles = [];
        for metric in metrics:
            data = pd.read_csv(f'data/dre_{ano}.csv', index_col=[0])
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
    
    if url == '/':
        regex = 'LIQUIDO'

        data = pd.read_csv(f'data/dre_{ano}.csv', index_col=[0])
        
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


@app.callback(
    Output('velocimeter', 'value'),
    Input('url', 'pathname'), Input('indicador-ano-dropdown', 'value')
)
def velocimeter(url, ano):
    
    if url == '/':
        # fig = go.Figure(
        #         go.Indicator(
        #             mode = "gauge+number+delta",
        #             value = 75,
        #             domain = {'x': [0, 1], 'y': [0, 1]},
        #             title = {'text': "Performance", 'font': {'size': 16}},
        #             delta = {'reference': 70, 'increasing': {'color': "green"}},
        #             gauge = {
        #                 'axis': {'range': [None, 100], 'tickwidth': 1},
        #                 'bar': {'color': "blue"},
        #                 'bgcolor': "white",
        #                 # 'borderwidth': 2,
        #                 # 'bordercolor': "gray",
        #                 'steps': [
        #                     {'range': [0, 30], 'color': 'red'},
        #                     {'range': [30, 70], 'color': 'yellow'},
        #                     {'range': [70, 100], 'color': 'green'}
        #                     ],
        #                 'threshold': {
        #                     'line': {'color': "cyan", 'width': 4},
        #                     'thickness': 0.75,
        #                     'value': 75
        #                     }
        #                 }
        #             )
        #         )

        # fig.update_layout(
        #     paper_bgcolor="lavender",
        #     font={'color': "darkblue", 'family': "Arial"}
        #     )

        value = np.random.randint(60, 100)

        return value


@app.callback(
    Output('progress-chart', 'figure'),
    Input('indicador-ano-dropdown', 'value'),
    Input('progress-dropdown', 'value'),
)
def progress_chart(ano, field):
    
    progress = np.random.randint(70, 100)
    
    df = pd.DataFrame({'names' : ['progress',' '],
                   'values' :  [progress, 100 - progress]})

    fig = px.pie(df, values ='values', hole = 0.6, 
                color_discrete_sequence = ['orange  ', 'rgba(0,0,0,0)']
                )

    fig.update_layout( 
                margin=dict(t=10, l=10, r=10, b=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',

                autosize=True,
                # minreducedwidth=250,
                # minreducedheight=250,
                # width=450,
                # height=450,
            )
    
    fig.data[0].textfont.color = 'white'
    
    return fig



@app.callback(
    Output('minigraph-1', 'figure'), Output('minigraph-1-title', 'children'),
    Output('minigraph-2', 'figure'), Output('minigraph-2-title', 'children'),

    Input('indicador-ano-dropdown', 'value'),
)
def update_mini_graphs(ano):
    
    data = pd.read_csv(f'data/dre_{ano}.csv', index_col=[0])

    field = 'LUCRO LIQUIDO'
    regex = 'LIQUIDO'

    y = data.loc[data['conta'].str.contains(regex)]
    op = y['tipo'].values[0]
    y = y.iloc[:, -12:]

    reversed = {}
    color = 'rgba(50, 171, 96, 0.6)' # green
    line_color = 'rgba(50, 171, 96, 1.0)'
    # if op == '-':
    #     color = 'rgba(245, 39, 39, 0.6)' # red
    #     line_color = 'rgba(245, 39, 39, 1.0)'
    #     reversed = {'yaxis': {'autorange': 'reversed'}}
    
    y = y.T.iloc[:, 0]

    fig = go.Figure()

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
            showlegend=False,
        ))

    fig.update_layout( 
                margin=dict(t=0, l=0, r=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                height=290,
                autosize=True,
                **reversed
            )

    title = field
    
    return fig, title, fig, title


### DADOS ###
@app.callback(
    Output('saved-data-table', 'data'),
    Input('url', 'pathname'), Input('dados-year-dropdown', 'value')
)
def update_saved_data_table(url, ano):
    if url == '/dados':
        saved_data = os.listdir('data')
        df_data = pd.DataFrame(data=saved_data, columns=['nome'])
        return df_data.to_dict('record')


@app.callback(
    Output('data-table', 'data'), Output('data-table-title', 'children'),
    Input('saved-data-table', 'selected_rows'), Input('saved-data-table', 'data'),
)
def show_selected_saved_table(row, data):
    row = [0] if row is None else row
    df_name = data[row[0]]['nome']
    df_to_load = pd.read_csv(f'data/{df_name}', index_col=[0])
    return df_to_load.to_dict('records'), df_name
        
        