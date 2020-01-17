from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ak8aJke2ppeEUjO&32KEd23IGEO3kuEhO84ueo'

from application import routes
