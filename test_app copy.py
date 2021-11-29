import pandas as pd
from sqlalchemy import create_engine, text

db = create_engine('postgresql://postgres:Tftabbzgf1.@localhost/postgres')

df = pd.read_sql(text("""SELECT "Час в дне", "День недели" FROM fes_out_db;"""), db)

df['Час в дне'] = df['Час в дне'].fillna(0)
df['День недели'] = df['День недели'].fillna(0)

print('Success!')

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

animations = {
    'Histogram Test': px.histogram(df, x="Час в дне", animation_frame="День недели"),
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
print ('Server run!')