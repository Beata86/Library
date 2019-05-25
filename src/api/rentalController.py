from src.api import app
from src.api import library
from flask import request
import json


@app.route('/rentals', methods=['POST'])
def addRental():
    bookNumber = int(request.form['bookNumber'])
    personNumber = int(request.form['personNumber'])
    library.addBookRental(bookNumber, personNumber)
    return str(len(library.bookRentals))


@app.route('/rentals', methods=['DELETE'])
def removeRental():
    rentalNumber = int(request.args.get('rentalNumber'))
    library.removeRental(rentalNumber)
    return str(len(library.bookRentals))


@app.route('/rentals')
def getRentals():
    jsonRentals = []
    for rental in library.bookRentals:
        jsonRental = {
            "book": {
                "title": rental.book.title,
                "author": rental.book.author
            },
            "person": {
                "name": rental.person.name,
                "surname": rental.person.surname,
                "gender": rental.person.sex,
                "age": rental.person.age,
                "height": rental.person.height
            }
        }
        jsonRentals.append(jsonRental)
    return json.dumps(jsonRentals)
