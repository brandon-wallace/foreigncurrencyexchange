# application/routes.py

from flask import render_template
from application import app
from application.forms import SelectionForm
import urllib.request
import json


def query_api():
    '''Query API for exchange rates'''

    try:
        url = 'https://api.exchangeratesapi.io/latest?base=USD'
        response = urllib.request.urlopen(url)
        data = response.read()
        text = json.loads(data)
        return text
    except Exception as e:
        print(e)


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Display home page'''

    amount = None
    form = SelectionForm(from_currency='USD', to_currency='MXN')
    text = query_api()
    if form.validate_on_submit():
        if form.from_currency.data == 'USD':
            amount = form.start_amount.data * 1 * text['rates'][form.to_currency.data]
        else:
            amount = form.start_amount.data / text['rates'][form.from_currency.data] 
    return render_template('index.html', form=form, amount=amount)


@app.errorhandler(404)
def page_not_found(error):
    '''Page not found'''

    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    '''Internal server error'''

    return render_template('500.html'), 500
