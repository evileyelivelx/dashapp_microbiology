import os
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import plotly.graph_objs as go

import plotly.express as px

dataframe = pd.read_csv('total_data_byareas.csv')

sample_date = pd.to_datetime(dataframe['SAMPLED_DATE']).dt.strftime("%Y-%m")
trace_close = px.scatter_mapbox(dataframe, lat='lat', lon='lon', hover_name="SAMPLE_NAME",
                                hover_data=['SAMPLE_NAME'], color="Detected", zoom=3, height=800,
                                size='Not Detected', animation_frame=sample_date,
                                title="Microbiology test result in different zones 2018 to 2019")

trace_close.update_layout(mapbox_style= "open-street-map", mapbox_accesstoken="pk.eyJ1IjoiZXZpbGV5ZWxpdmUiLCJhIjoiY2s1ajZtMnp0MDA1YjNvcWw4eHViNzlnNSJ9.VbbcjnLg9sNJ26uiR6DN2A")
trace_close.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id="graph_close",
                figure={
                    "data": [trace_close],
                    "layout": {
                        "title": "Close Graph"
                    }
                }
            )
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)