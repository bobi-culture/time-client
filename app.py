from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Time Client !!! </h1>";

@app.route("/gettime")
def get_time():
    response = requests.get('localhost:5000/api/time')
    json_response = response.json()
    data = json_response['time']
    return f"<font face=tahoma size=20 color=red>{data}</font>"