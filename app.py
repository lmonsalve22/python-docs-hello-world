from flask import Flask
import dash
#import dash_core_components as dcc
#import dash_html_components as html
#
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import pandas as pd
import dash_bootstrap_components as dbc
import pandas_datareader.data as web
import datetime
import dash_html_components as html
import dash_core_components as dcc
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from flask import Flask
"""
#app = Flask(__name__)

server = Flask(__name__)
df = pd.read_csv("mystocks.csv")

app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/'
)

app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H1("Stock Market Dashboard",
                        className='text-center text-primary mb-4'),
                width=12)
             )], fluid=True)


#Sentencias para abrir el servidor al ejecutar este script
#if __name__ == '__main__':
#    app.run_server(port=7000)
#@app.route("/")
#def hello():
#    return "Hello, World! 2.1"

@server.route("/dash")
def hello():
    #return app.index()
    return "Hello, World!"
