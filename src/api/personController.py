from src.api import app
from src.api import library
from flask import request
import json

@app.route('/persons', methods=['POST'])
def addPerson():
    name = request.form['name']
    surname = request.form['surname']
    gender = request.form['gender']
    age = int(request.form['age'])
    height = int(request.form['height'])
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
