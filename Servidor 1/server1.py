from flask import Flask, jsonify, json, request, abort, request
from bson import json_util
import requests

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def getNotes():
    x = requests.get('http://3.21.163.239:5000/notes')
    data = x.json()
    return data

@app.route('/getram', methods=['GET'])
def getRAM():
    return "RAM: 22%"

@app.route('/getcpu', methods=['GET'])
def getCPU():
    return "CPU: 12%"

@app.route('/addnote', methods=['POST'])
def addNote():
    #before make the request, verify wich server to select on your resources
    json_ = request.json
    x = requests.post(url='http://3.21.163.239:5000/addnote', json=json_)
    respon = x.json()
    return respon


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)