from src.api import app
from src.api import library
from src.library.BookInRentalException import BookInRentalException
from flask import request
import json

@app.route('/books', methods=['POST'])
def addBook():
    title = request.form['title']
    author = request.form['author']
    library.addBook(title, author)
    return str(len(library.books))

@app.route('/books', methods=['DELETE'])
def removeBook():
    bookNumber = int(request.args.get('bookNumber'))
    library.removeBook(bookNumber)
    return str(len(library.books))

@app.route('/books')
def getBooks():
    jsonBooks = []
    for book in library.books:
        jsonBook = {
            "title": book.title,
            "author": book.author
        }
        jsonBooks.append(jsonBook)
    return json.dumps(jsonBooks)

@app.errorhandler(BookInRentalException)
def handleBookRentalException(e):
    return 'Książka jest aktualnie w wypożyczeniu', 400