
from flask import Flask
app = Flask(__name__)

import src.api.views # noqa
