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

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! 2.1"
