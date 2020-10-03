from flask import Flask, jsonify, json, request, abort
from bson import json_util
import connectDB
    
app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def getNotes():
    docs_list  = list(connectDB.getNotes())
    return jsonify({'notes': json.loads(json.dumps(docs_list, default=json_util.default))})

@app.route('/addnote', methods=['POST'])
def addNote():
    status = connectDB.insertNote(request.json['autor'], request.json['nota'])
    if status == 200:
       return jsonify({'message': 'Nota agregada correctamente.'}) 
    else:
        return jsonify({'message': 'No se pudo agregar la nota.'})

@app.route('/getram', methods=['GET'])
def getRAM():
    archivo = open("/proc/RAM_201503911","r")
    lineas = archivo.readlines()
    archivo.close()
    if len(lineas)>0:
        return jsonify({'lineas': lineas})
    else:
        return jsonify({'lineas': 'No se pudo leer el modulo.'})

@app.route('/getcpu', methods=['GET'])
def getCPU():
    return "CPU: 15%"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)