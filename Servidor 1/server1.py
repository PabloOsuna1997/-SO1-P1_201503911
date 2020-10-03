from flask import Flask, jsonify, json, request, abort, request
from bson import json_util
import requests

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def getNotes():
    x = requests.get('http://18.220.134.88:5000/notes')
    data = x.json()
    return data

@app.route('/getres', methods=['GET'])
def getRAM():    
    resA = getResourcesServerA()
    resB = getResourcesServerB()
    return jsonify({'resources_A':resA, 'resources_B':resB})

def getResourcesServerA():
    x = requests.get('http://18.220.134.88:5000/getram')
    data = x.json()
    tmp = data['lineas'][1].split(':')
    ram = tmp[1]
    x = requests.get('http://18.220.134.88:5000/notes')
    data = x.json()
    resA = {'RAM': int(ram[0:len(ram)-1]), 'Len': len(data['notes']), 'cpu': 4}
    return resA

def getResourcesServerB():
    x = requests.get('http://18.220.134.88:5000/getram')
    data = x.json()
    tmp = data['lineas'][1].split(':')
    ram = tmp[1]
    x = requests.get('http://18.220.134.88:5000/notes')
    data = x.json()
    resB = {'RAM': int(ram[0:len(ram)-1]), 'Len': len(data['notes']), 'cpu': 2}
    return resB

@app.route('/addnote', methods=['POST'])
def addNote():
    #before make the request, verify wich server to select on your resources

    json_ = request.json
    x = requests.post(url='http://18.220.134.88:5000/addnote', json=json_)
    respon = x.json()
    return respon


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)      #correra en el puerto 5001