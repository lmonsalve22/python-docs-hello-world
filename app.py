from flask import Flask
import dash
#import dash_core_components as dcc
#import dash_html_components as html
#from dash.dependencies import Output, Input
#import plotly.express as px
#import dash_bootstrap_components as dbc
import pandas as pd
#import pandas_datareader.data as web
import datetime
import dash_core_components as dcc
import dash_html_components as html
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
    ),

    dbc.Row([

        dbc.Col([
            dcc.Dropdown(id='my-dpdn', multi=False, value='AMZN',
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['Symbols'].unique())],
                         ),
            dcc.Graph(id='line-fig', figure={})
        ],# width={'size':5, 'offset':1, 'order':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dcc.Dropdown(id='my-dpdn2', multi=True, value=['PFE','BNTX'],
                         options=[{'label':x, 'value':x}
                                  for x in sorted(df['Symbols'].unique())],
                         ),
            dcc.Graph(id='line-fig2', figure={})
        ], #width={'size':5, 'offset':0, 'order':2},
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

    ], no_gutters=True, justify='start'),  # Horizontal:start,center,end,between,around

    dbc.Row([
        dbc.Col([
            html.P("Select Company Stock:",
                   style={"textDecoration": "underline"}),
            dcc.Checklist(id='my-checklist', value=['FB', 'GOOGL', 'AMZN'],
                          options=[{'label':x, 'value':x}
                                   for x in sorted(df['Symbols'].unique())],
                          labelClassName="mr-3"),
            dcc.Graph(id='my-hist', figure={}),
        ], #width={'size':5, 'offset':1},
            #clase de bootstrap para tamaños de pantallas
           xs=12, sm=12, md=12, lg=5, xl=5
        ),

        dbc.Col([
            dbc.Card(
                [
                    dbc.CardBody(
                        html.P(
                            "We're better together. Help each other out!",
                            className="card-text")
                    ),
                    dbc.CardImg(
                        src="https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif",
                        bottom=True),
                ],
                style={"width": "24rem"},
            )
        ], #width={'size':5, 'offset':1},
           xs=12, sm=12, md=12, lg=5, xl=5
        )
    ], align="center")  # Vertical: start, center, end

], fluid=True)

# Callback section: connecting the components
# ************************************************************************
# Line chart - Single

@app.callback(
    Output('line-fig', 'figure'),
    Input('my-dpdn', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='Date', y='High')
    return figln


# Line chart - multiple
@app.callback(
    Output('line-fig2', 'figure'),
    Input('my-dpdn2', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    figln2 = px.line(dff, x='Date', y='Open', color='Symbols')
    return figln2


# Histogram
@app.callback(
    Output('my-hist', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    dff = dff[dff['Date']=='2020-12-03']
    fighist = px.histogram(dff, x='Symbols', y='Close')
    return fighist

#Sentencias para abrir el servidor al ejecutar este script
#if __name__ == '__main__':
#    app.run_server(port=7000)
#@app.route("/")
#def hello():
#    return "Hello, World! 2.1"

@server.route("/dash")
def hello():
    return app.index()
