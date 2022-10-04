from flask import Flask
from dynaconf import FlaskDynaconf
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)
    app.config.from_pyfile('./config.py')
    csrf = CSRFProtect(app)

    return app
