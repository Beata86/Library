from src.library.Library import *
from flask import Flask

app = Flask(__name__)
library = Library()

import src.api.bookController # noqa
import src.api.personController # noqa
import src.api.viewController # noqa