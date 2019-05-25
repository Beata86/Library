from src.library.Library import Library
from flask import Flask
from src.library.LibraryInitialization import initializeLibrary

app = Flask(__name__)
library = Library()
initializeLibrary(library)

import src.api.bookController # noqa
import src.api.personController # noqa
import src.api.viewController # noqa
import src.api.rentalController # noqa