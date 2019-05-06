from src.api import app
# from flask import request

@app.route('/')
def index():
    return "Kalafior to dziad"

