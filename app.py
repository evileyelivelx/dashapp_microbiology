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

# trace_map = go.Scattermapbox(
#     lat=dataframe['lat'],
#     lon=dataframe['lon'],
#     mode='markers',
#     marker=go.scattermapbox.Marker(
#         size=dataframe['Detected'],
#         color=dataframe['Not Detected'],
#         opacity=0.7
#     ),
#     text=dataframe['SAMPLE_NAME'],
#     hoverinfo='text',
#
# )

# layout_map = dict(
#     title='map',
#     autosize=True,
#     hovermode='closest',
#     showlegend=True,
#     mapbox=go.layout.Mapbox(
#         accesstoken=mapbox_token,
#         bearing=0,
#         center=go.layout.mapbox.Center(
#             lat=-41.57623,
#             lon=173.27493,
#         ),
#         zoom=12,
#         style='open-street-map'
#     ),
# )
# px.set_mapbox_access_token(open(mapbox_token).read())

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

# app.layout = html.Div([
#     html.Div(html.H2(children="Microbiology test result from 2018.01 to 2019.11")),
#
#     html.Div(children='''Bar chart'''),
#     dcc.Graph(
#         id='Data by zones',
#         figure=fig
#     ),
#
#     html.Div(children='''Bar chart2'''),
#     dcc.Graph(
#         id='Data by zones2',
#         figure=fig
#     ),
#
#
# ])

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

            html.Div(children='''Dash: A web to show result''', className='nine columns')
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
                    id='date-slider',
                    min=dataframe['Num'].min(),
                    max=dataframe['Num'].max(),
                    value=dataframe['Num'].min(),
                    marks={str(year): str(year) for year in dataframe['Num'].unique()},
                    step=0.5,

                )
            ], className='ten columns'),
        ])
    ])
)

@app.callback(
    Output('map-slider', 'figure'),
    [Input('date-slider', 'value')]
)

def update_figure(selected_year):
    filtered_df = dataframe[dataframe['Num'] == selected_year]
    traces = []
    for i in filtered_df['SAMPLE_NAME'].unique():
        df_by_zone = filtered_df[filtered_df['SAMPLE_NAME'] == i]
        new_trace = go.Scattermapbox(
            lat=df_by_zone['lat'],
            lon=df_by_zone['lon'],
            mode='markers',
            marker={"size": df_by_zone['Detected']+10,
                    "color": df_by_zone['Not Detected']},
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
        title=dict(text="Result show on the map", font=dict(size=30, color='blue')),
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





if __name__ == '__main__':
    app.run_server(debug=True)