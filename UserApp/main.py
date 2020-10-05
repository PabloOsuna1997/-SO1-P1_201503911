import ast
import json
import sys
import requests

contentFile = ""
path = ""
sentences = ""
authors = ""
contentFileA = ""
txtJson = ""
ObjectJson = any

ipServer1 = 'http://18.189.22.240:5001'

class NoteObject():
    def getNotes(self):
        x = requests.get(ipServer1 + '/notes')
        data = x.json()
        return data

    def addNote(self, autor, nota ):
        x = requests.post(url= ipServer1 + '/addnote', json={'autor':autor, 'nota':nota})
        return x

class Menu():
    def __init__(self):
        global contentFile, path, sentences, objects, authors, contentFileA, txtJson, ObjectJson
        txtJson = ""
        option = input("Seleccione una opcion: \n1. Ingrese una ruta.\n"+
            "2. Ingresar direccion.\n"+
            "3. Ver datos.\n"+
            "4. Enviar datos.\n"+   
            "5. Ver datos de la bd.\n" +
            "6. Salir.\n")

        if option == "1":
            try:
                #sentences
                #pathTmp = input("Ingrese ruta del archivo: \n")
                file = open("./texto.txt")
                contentFile = file.read()
                print("Cargando Archivo...\n")
                file.close()
                #authors
                file = open("./autores.txt")
                contentFileA = file.read()
                file.close()

                sentences = contentFile.split('.\n')
                authors = contentFileA.split('.\n')
                i = 0
                txtJson += '{ "objetos": ['            
                while i < len(sentences):
                    txtJson += "{"
                    txtJson += f''' "autor": "{authors[i]}",'''
                    txtJson += f''' "nota" : "{sentences[i]}" '''
                    txtJson += "}"
                    if i+1 < len(sentences):
                        txtJson += ","
                    i += 1
                txtJson += ']}'
                ObjectJson = json.loads(txtJson)
                #print(ObjectJson)

            except:
                print("No se encontro el archivo.\n")

        elif option == "2":
            pathTmp = input("Ingrese una direccion: \n")
            path = pathTmp
            print(pathTmp)

        elif option == "3":
            note = NoteObject()
            if len(sentences)> 0:
                print(sentences)
            else: 
                print("Actualmente no hay notas preparadas para enviar.")
        
        elif option == "4":
            try:
                notePost = NoteObject()
                for object in ObjectJson['objetos']:
                    response = notePost.addNote(object['autor'],object['nota'])
                print("Enviando datos..\n")
            except:
                print("No se pudieron agregar todos los registros")
        elif option == "5":
            notes = NoteObject()
            print(notes.getNotes())
        elif option == "6":
            print("Adios..\n")
            sys.exit()
        else:
            print("Opcion no valida.\n")
        print("\n")



if  __name__ == "__main__":
    print("Ingrese una Opcion: \n")
    #para ejecutar un comando en el sistema operativo
    #import subprocess
    #subprocess.run(["python", "--version"])
    while 1:
        menu = Menu()
    sys.exit()