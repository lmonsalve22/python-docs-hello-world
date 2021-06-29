from flask import Flask
import geemap

app = Flask(__name__)

@app.route("/")
def hello():
    Map = geemap.Map(center=(40, -100), zoom=4)    
    return Map