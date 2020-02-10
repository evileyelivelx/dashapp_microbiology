import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go
from datetime import datetime as dt

import plotly.express as px

# All zone datas
"""All tables"""
dataframe = pd.read_csv('total_data_byareas.csv')
sample_date = pd.to_datetime(dataframe['SAMPLED_DATE']).dt.strftime("%Y-%m")

db_zone1 = dataframe[dataframe['Areas'] == 'Zone 1']
zone_date1 = pd.to_datetime(db_zone1['SAMPLED_DATE']).dt.strftime("%Y-%m")

db_zone2 = dataframe[dataframe['Areas'] == 'Zone 2']
zone_date2 = pd.to_datetime(db_zone2['SAMPLED_DATE']).dt.strftime("%Y-%m")

db_zone3 = dataframe[dataframe['Areas'] == 'Zone 3']
zone_date3 = pd.to_datetime(db_zone3['SAMPLED_DATE']).dt.strftime("%Y-%m")

db_zone4 = dataframe[dataframe['Areas'] == 'Zone 4']
zone_date4 = pd.to_datetime(db_zone4['SAMPLED_DATE']).dt.strftime("%Y-%m")

dates = {"2018-01":0,
         "2018-02":2,
         "2018-03":4,
         "2018-04":6,
         "2018-05":8,
         "2018-06":10,
         "2018-07":12,
         "2018-08":14,
         "2018-09":16,
         "2018-10":18,
         "2018-11":20,
         "2018-12":22,
         "2019-01":24,
         "2019-02":26,
         "2019-03":28,
         "2019-04":30,
         "2019-05":32,
         "2019-06":34,
         "2019-07":36,
         "2019-08":38,
         "2019-09":40,
         "2019-10":42,
         "2019-11":44,
         "2019-12":46


}

dataframe['Number'] = dataframe['SAMPLED_DATE'].map(dates)

"""individual zones"""


mapbox_token = "pk.eyJ1IjoiZXZpbGV5ZWxpdmUiLCJhIjoiY2s1ajZtMnp0MDA1YjNvcWw4eHViNzlnNSJ9.VbbcjnLg9sNJ26uiR6DN2A"

trace_zone1 = go.Bar(
        x=zone_date1,
        y=db_zone1['Detected'],
        name='Detected',
        marker_color='rgb(55, 83, 109)'
)
trace_zone1_2 = go.Bar(
        x=zone_date1,
        y=db_zone1['Not Detected'],
        name='Not Detected',
        marker_color='rgb(26, 118, 255)'
)
trace_zone1_3 = go.Bar(
        x=zone_date1,
        y=db_zone1['Presumptive positive'],
        name='Presumptive positive',
        marker_color='rgb(105, 82, 22)'
)

trace_zone2 = go.Bar(
        x=zone_date2,
        y=db_zone2['Detected'],
        name='Detected',
        marker_color='rgb(55, 83, 109)'
)
trace_zone2_2 = go.Bar(
        x=zone_date2,
        y=db_zone2['Not Detected'],
        name='Not Detected',
        marker_color='rgb(26, 118, 255)'
)
trace_zone2_3 = go.Bar(
        x=zone_date2,
        y=db_zone2['Presumptive positive'],
        name='Presumptive positive',
        marker_color='rgb(105, 82, 22)'
)

trace_zone3 = go.Bar(
        x=zone_date3,
        y=db_zone3['Detected'],
        name='Detected',
        marker_color='rgb(55, 83, 109)'
)
trace_zone3_2 = go.Bar(
        x=zone_date3,
        y=db_zone3['Not Detected'],
        name='Not Detected',
        marker_color='rgb(26, 118, 255)'
)
trace_zone3_3 = go.Bar(
        x=zone_date3,
        y=db_zone3['Presumptive positive'],
        name='Presumptive positive',
        marker_color='rgb(105, 82, 22)'
)

trace_zone4 = go.Bar(
        x=zone_date4,
        y=db_zone4['Detected'],
        name='Detected',
        marker_color='rgb(55, 83, 109)'
)
trace_zone4_2 = go.Bar(
        x=zone_date4,
        y=db_zone4['Not Detected'],
        name='Not Detected',
        marker_color='rgb(26, 118, 255)'
)
trace_zone4_3 = go.Bar(
        x=zone_date4,
        y=db_zone4['Presumptive positive'],
        name='Presumptive positive',
        marker_color='rgb(105, 82, 22)'
)

data1 = [trace_zone1, trace_zone1_2, trace_zone1_3]
data2 = [trace_zone2, trace_zone2_2, trace_zone2_3]
data3 = [trace_zone3, trace_zone3_2, trace_zone3_3]
data4 = [trace_zone4, trace_zone4_2, trace_zone4_3]

layout1 = dict(title="Zone 1 data",
              showlegend=True)
layout2 = dict(title="Zone 2 data",
              showlegend=True)
layout3 = dict(title="Zone 3 data",
              showlegend=True)
layout4 = dict(title="Zone 4 data",
              showlegend=True)



trace_map = px.scatter_mapbox(dataframe, lat='lat', lon='lon', color="Detected",
                              size='Not Detected', color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=12)

data_map = [trace_map]

fig1 = dict(data=data1, layout=layout1)
fig2 = dict(data=data2, layout=layout2)
fig3 = dict(data=data3, layout=layout3)
fig4 = dict(data=data4, layout=layout4)
fig5 = dict(data=data_map, layout=dict(title='xx'))

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server



app.layout = html.Div(
    html.Div([
        html.Div([
            html.H1(children="Data Analysis for Microbiology", className='nine columns'),
            html.Img(src="assets/cawthron-institute-logo-2.png",
                     className='three columns',
                     style={
                         "height": '9%',
                         'width': "9%",
                         'float': 'right',
                         'position': 'relative',
                         "margin-top": 10
                     }),

            html.Div(children='''Dashboard: A web application to show result''', className='nine columns')
        ], className='row'),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='Zone 1',
                    figure=fig1,
                )
            ], className='six columns'),

            html.Div([
                dcc.Graph(
                    id='Zone 2',
                    figure=fig2
                )
            ], className='six columns')
        ]),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='Zone 3',
                    figure=fig3
                )
            ], className='six columns'),

            html.Div([
                dcc.Graph(
                    id='Zone 4',
                    figure=fig4
                )
            ], className='six columns')
        ]),

        html.Div([
            html.Div([
                dcc.Graph(id='map-slider'),
                dcc.Slider(
                    id='year-slider',
                    min=0,
                    max=46,
                    value=2,
                    marks={
                        0: "2018-01",
                        2: "2018-02",
                        4: "2018-03",
                        6: "2018-04",
                        8: "2018-05",
                        10: "2018-06",
                        12: "2018-07",
                        14: "2018-08",
                        16: "2018-09",
                        18: "2018-10",
                        20: "2018-11",
                        22: "2018-12",
                        24: "2019-01",
                        26: "2019-02",
                        28: "2019-03",
                        30: "2019-04",
                        32: "2019-05",
                        34: "2019-06",
                        36: "2019-07",
                        38: "2019-08",
                        40: "2019-09",
                        42: "2019-10",
                        44: "2019-11",
                        46: "2019-12"
                    },
                    step=None

                )
            ], className='ten columns'),
        ]),

        html.Div([
            html.Div([
                dcc.Graph(
                    id='pie-chart',
                ),
                html.Div([
                    dcc.Slider(
                        id='pie-slider',
                        min=0,
                        max=46,
                        value=8,
                        marks={
                            0: "2018-01",
                            2: "2018-02",
                            4: "2018-03",
                            6: "2018-04",
                            8: "2018-05",
                            10: "2018-06",
                            12: "2018-07",
                            14: "2018-08",
                            16: "2018-09",
                            18: "2018-10",
                            20: "2018-11",
                            22: "2018-12",
                            24: "2019-01",
                            26: "2019-02",
                            28: "2019-03",
                            30: "2019-04",
                            32: "2019-05",
                            34: "2019-06",
                            36: "2019-07",
                            38: "2019-08",
                            40: "2019-09",
                            42: "2019-10",
                            44: "2019-11",
                            46: "2019-12"
                        },
                    )
                ], style={'textAlign': "center", "margin": "30px", "padding": "10px", "width": "65%",
                               "margin-left": "auto",
                               "margin-right": "auto"})
            ], className="ten columns")
        ])
    ])
)

@app.callback(
    Output('map-slider', 'figure'),
    [Input('year-slider', 'value')]
)

def update_figure(selected_year):
    filtered_df = dataframe[dataframe['Number'] == selected_year]
    traces = []
    for i in filtered_df['SAMPLE_NAME'].unique():
        df_by_zone = filtered_df[filtered_df['SAMPLE_NAME'] == i]
        new_trace = go.Scattermapbox(
            lat=df_by_zone['lat'],
            lon=df_by_zone['lon'],
            mode='markers',
            marker={"size": df_by_zone['Detected']+20,
                    "color": df_by_zone['Not Detected']*10},
            showlegend=True,
            text=df_by_zone['Detected'],
            name=i,
            hovertext=df_by_zone['Detected']

        )
        traces.append(new_trace)

    layout_map = go.Layout(
        showlegend=True,
        autosize=True,
        hovermode='closest',
        title=dict(text="Result show on the map", font=dict(size=25, color='Black')),
        # margin={'l': 50, 'b': 40, 't': 10, 'r': 10},
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=-41.256783,
                lon=173.279274
            ),
            pitch=0,
            zoom=15,
            style='open-street-map'
        )
    )

    return {
        'data': traces,
        'layout': layout_map
    }

@app.callback(
    Output("pie-chart", 'figure'),
    [Input('pie-slider', 'value')]
)
def update_pie(selected):
    return {
        "data": [go.Pie(labels=dataframe['SAMPLE_NAME'].unique().tolist(), values=dataframe[dataframe['Number'] == selected]['Detected'].tolist(),
                        marker={'colors': [dataframe['Detected']+50]}, textinfo='label')],
        "layout": go.Layout(title=f"Pie Chart Result by Different Zones 2018.01-2019.12", margin={"l": 200, "r": 200, "t": 100},
                            legend={"x": 1, "y": 0.7})
    }



if __name__ == '__main__':
    app.run_server(debug=True)