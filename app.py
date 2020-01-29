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

#
# trace_close = px.scatter_mapbox(dataframe, lat='lat', lon='lon', hover_name="SAMPLE_NAME",
#                                 hover_data=['SAMPLE_NAME'], color="Detected", zoom=3, height=600,
#                                 size='Not Detected', animation_frame=sample_date,
#                                 title="Data by zones from 2018.01 to 2019.12", width=700)
#
# trace_close.update_layout(mapbox_style= "open-street-map", mapbox_accesstoken="pk.eyJ1IjoiZXZpbGV5ZWxpdmUiLCJhIjoiY2s1ajZtMnp0MDA1YjNvcWw4eHViNzlnNSJ9.VbbcjnLg9sNJ26uiR6DN2A")
# trace_close.update_layout(margin={"r":5,"t":5,"l":5,"b":10})

trace_close1 = go.Bar(
        x=sample_date,
        y=dataframe['Detected'],
        name='Detected',
        marker_color='rgb(55, 83, 109)'
)
trace_close2 = go.Bar(
        x=sample_date,
        y=dataframe['Not Detected'],
        name='Not Detected',
        marker_color='rgb(26, 118, 255)'
)

trace_close3 = go.Bar(
        x=sample_date,
        y=dataframe['Presumptive positive'],
        name='Presumptive positive',
        marker_color='rgb(105, 82, 22)'
)

# trace_close = go.Figure()
# trace_close.add_trace(
#     go.Bar(
#         x=sample_date,
#         y=dataframe['Detected'],
#         name='Detected',
#         marker_color='rgb(55, 83, 109)'
#     )
# )
# trace_close.add_trace(
#     go.Bar(
#         x=sample_date,
#         y=dataframe['Not Detected'],
#         name='Not Detected',
#         marker_color='rgb(26, 118, 255)'
#     )
# )
# trace_close.add_trace(
#     go.Bar(
#         x=sample_date,
#         y=dataframe['Presumptive positive'],
#         name='Presumptive positive',
#         marker_color='rgb(105, 82, 22)'
#     )
# )

data = [trace_close1, trace_close2, trace_close3]

layout = dict(title="Bar Chart",
              showlegend=True)

fig = dict(data=data, layout=layout)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.Div(html.H1(children="Microbiology test result from 2018.01 to 2019.11")),
    html.Label("All zones"),
    html.Div(
        dcc.Graph(id="Data by zones",
                  figure=fig)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)