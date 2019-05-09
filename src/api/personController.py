from src.api import app
from src.api import library
from flask import request
import json

@app.route('/persons', methods=['POST'])
def addPerson():
    name = request.args.get('name')
    surname = request.args.get('surname')
    gender = request.args.get('gender')
    age = int(request.args.get('age'))
    height = int(request.args.get('height'))
    library.addPerson(name, surname, gender, age, height)
    return str(len(library.persons))

@app.route('/persons')
def getPersons():
    jsonPersons = []
    for person in library.persons:
        jsonPerson = {
            "name": person.name,
            "surname": person.surname,
            "gender": person.sex,
            "age": person.age,
            "height": person.height
        }
        jsonPersons.append(jsonPerson)
    return json.dumps(jsonPersons)
