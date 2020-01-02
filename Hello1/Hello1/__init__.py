"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import Hello1.views
import Hello1.service_functions

# A comment just to make sure it synced
