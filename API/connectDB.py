from pymongo import MongoClient

#connection to database
clientM = MongoClient('mongo')   #se conectara al servicio que se llama mongo
db = clientM['dbProyecto1-sopes1']
notes = db['Note']

#insert element for add mores objects use insert_many with list of python
def insertNote (autor, nombre):
    try:
        notes.insert_one(
            {
                'autor': autor,
                'nota': nombre
            }
        )
        return 200
    except:
        return 500   

def getNotes ():
    return notes.find({})