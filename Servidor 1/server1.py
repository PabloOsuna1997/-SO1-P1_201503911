from flask import Flask, jsonify, json, request, abort, request
from flask_cors import CORS
from bson import json_util
import requests

app = Flask(__name__)
CORS(app)
ipA = 'http://18.188.24.81:5000'
ipB = 'http://18.188.24.81:5000'

@app.route('/notes', methods=['GET'])
def getNotes():
    x = requests.get(ipA + '/notes')            #IP SERVER A
    data = x.json()
    return data

@app.route('/getres', methods=['GET'])
def getRAM():    
    resA = getResourcesServerA()
    resB = getResourcesServerB()
    return jsonify({'resources_A':resA, 'resources_B':resB})

def getResourcesServerA():
    x = requests.get(ipA + '/getram')           #IP SERVER A
    data = x.json()
    tmp = data['lineas'][1].split(':')
    ram = tmp[1]
    x = requests.get(ipA + '/notes')            #IP SERVER A
    data = x.json()
    resA = {'RAM': int(ram[0:len(ram)-1]), 'Len': len(data['notes']), 'cpu': 4}
    return resA

def getResourcesServerB():
    x = requests.get(ipB + '/getram')           #IP SERVER B
    data = x.json()
    tmp = data['lineas'][1].split(':')
    ram = tmp[1]
    x = requests.get(ipB + '/notes')            #IP SERVER B
    data = x.json()
    resB = {'RAM': int(ram[0:len(ram)-1]), 'Len': len(data['notes']), 'cpu': 2}
    return resB

@app.route('/addnote', methods=['POST'])
def addNote():
    #before make the request, verify wich server to select on your resources
    resA = getResourcesServerA()
    resB = getResourcesServerB()
    decision = 0      # 0 is A, 1 is B
    if resB['RAM'] > resA['RAM']:
        decision = 1
    elif resB['Len'] > resA['Len']:
        decision = 1
    elif resB['cpu'] > resA['cpu']:
        decision = 1
    else:
        decision = 0
    
    if decision == 0:
        json_ = request.json
        x = requests.post(url=ipA + '/addnote', json=json_)             #IP SERVER WINNER A
        respon = x.json()
        print("###   A    ###")
        return respon
    else:
        json_ = request.json
        x = requests.post(url=ipB + '/addnote', json=json_)             #IP SERVER WINNER B
        respon = x.json()
        print("###   B    ###")
        return respon

@app.route('/', methods=['GET'])
def index():
    return {'message': 'Bienvenido al servidor 1.'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)      #correra en el puerto 5001