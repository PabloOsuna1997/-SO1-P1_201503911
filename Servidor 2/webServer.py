from flask import Flask, jsonify, json, request, abort, request
from flask_cors import CORS
from bson import json_util
import requests

app = Flask(__name__)
CORS(app)
ipA = 'http://18.222.190.190:5000'
ipB = 'http://3.20.235.39:5000'

@app.route('/notesA', methods=['GET'])
def getNotes():
    x = requests.get(ipA + '/notes')            #IP SERVER A
    data = x.json()
    return data
@app.route('/notesB', methods=['GET'])
def getNotesB():
    x = requests.get(ipB + '/notes')            #IP SERVER A
    data = x.json()
    return data

@app.route('/getresA', methods=['GET'])
def getresA():    
    x = requests.get(ipB + '/getres')            #IP SERVER A
    data = x.json()
    return data


@app.route('/getresB', methods=['GET'])
def getresB():    
    x = requests.get(ipB + '/getres')            #IP SERVER A
    data = x.json()
    return data


@app.route('/', methods=['GET'])
def index():
    return {'message': 'Bienvenido al servidor 2.'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)      #correra en el puerto 5001