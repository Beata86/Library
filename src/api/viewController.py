from src.api import app
from flask import send_from_directory, redirect
import src.serverMain as serverMain
import os


@app.route('/html/<path:path>')
def send_html(path):
    rootPath = os.path.dirname(serverMain.__file__)
    return send_from_directory(rootPath + '/webapp/html', path)

@app.route('/')
def hello():
    return redirect("/html/manageBooks.html")