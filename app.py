import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go

import plotly.express as px

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
""""""

#
# trace_close = px.scatter_mapbox(dataframe, lat='lat', lon='lon', hover_name="SAMPLE_NAME",
#                                 hover_data=['SAMPLE_NAME'], color="Detected", zoom=3, height=600,
#                                 size='Not Detected', animation_frame=sample_date,
#                                 title="Data by zones from 2018.01 to 2019.12", width=700)
#
# trace_close.update_layout(mapbox_style= "open-street-map", mapbox_accesstoken="pk.eyJ1IjoiZXZpbGV5ZWxpdmUiLCJhIjoiY2s1ajZtMnp0MDA1YjNvcWw4eHViNzlnNSJ9.VbbcjnLg9sNJ26uiR6DN2A")
# trace_close.update_layout(margin={"r":5,"t":5,"l":5,"b":10})
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

data1 = [trace_zone1, trace_zone1_2, trace_zone1_3]
data2 = [trace_zone2, trace_zone2_2, trace_zone2_3]

layout = dict(title="Bar Chart",
              showlegend=True)

fig1 = dict(data=data1, layout=layout)
fig2 = dict(data=data2, layout=layout)

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
            html.Div(children='''Dash: A web to show result''', className='nine columns')
        ], className='row'),

        html.Div([
            dcc.Graph(
                id='Zone 1',
                figure=fig1
            )
        ], className='six columns'),

        html.Div([
            dcc.Graph(
                id='Zone 2',
                figure=fig2
            )
        ], className='six columns'),
    ])
)


if __name__ == '__main__':
    app.run_server(debug=True)