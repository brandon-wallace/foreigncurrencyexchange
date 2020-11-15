import os
from flask import Flask

app = Flask(__name__)

from application import routes

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
