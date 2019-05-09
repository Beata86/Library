from src.api import app
from src.api import library
from flask import request
import json

@app.route('/books', methods=['POST'])
def addBook():
    title = request.args.get('title')
    author = request.args.get('author')
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

