#! apps/__init__.py

from flask import Flask
from apps.routes import apis

app = Flask(__name__)
app.register_blueprint(apis)
