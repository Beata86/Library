from src.api import app
from src.api import library
from flask import request

@app.route('/person', methods=['POST'])
def addPerson():
    name = request.args.get('name')
    surname = request.args.get('surname')
    gender = request.args.get('gender')
    age = int(request.args.get('age'))
    height = int(request.args.get('height'))
    library.addPerson(name, surname, gender, age, height)
    return str(len(library.persons))