import pandas as pd

df = pd.read_excel('/Users/foxjap/Downloads/RC_F01_01_2019_T26_11_2021.xlsx', 0, header=0, index_col=None, na_values=["NA"])

print('Import from database success!')

df['month'] = pd.DatetimeIndex(df['DT']).month
df['year'] = pd.DatetimeIndex(df['DT']).year
#df['vol'] = df['vol'].dropna
#display(df)

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

animations = {
    'Scatter': px.scatter(
        df, x="vol", y="ruo", animation_frame="month", 
        animation_group="year", size="ruo", color="vol", 
        hover_name="year", log_x=True, size_max=55, 
        range_x=[20,400], range_y=[2,10]),
    'Bar': px.bar(
        df, x="vol", y="ruo", color="vol", 
        animation_frame="month", animation_group="month", 
        range_x=[20,400], range_y=[2,10]),
}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=[{'label': x, 'value': x} for x in animations],
        value='Scatter'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("selection", "value")])
def display_animated_graph(s):
    return animations[s]

app.run_server(debug=True)