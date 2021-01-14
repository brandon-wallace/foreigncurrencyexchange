from os import environ
from flask import Flask

app = Flask(__name__)

from application import routes

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['API_KEY'] = environ.get('API_KEY')
