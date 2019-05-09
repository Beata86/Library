from src.api import app
from src.api import library
from flask import request

@app.route('/book', methods=['POST'])
def addBook():
    title = request.args.get('title')
    author = request.args.get('author')
    library.addBook(title, author)
    return str(len(library.books))

@app.route('/book', methods=['DELETE'])
def removeBook():
    bookNumber = int(request.args.get('bookNumber'))
    library.removeBook(bookNumber)
    return str(len(library.books))