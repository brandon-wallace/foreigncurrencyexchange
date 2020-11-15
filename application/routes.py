# application/routes.py

import json
import urllib
from datetime import datetime, date, timedelta
from flask import render_template, url_for, redirect
from application import app
from application.forms import SelectionForm

today = date.today()
rate_30_ago = today - timedelta(days=30)
rate_90_ago = today - timedelta(days=90)


def query_api():
    '''Query API for exchange rates'''

    try:
        url = 'https://api.exchangeratesapi.io/latest?base=USD'
        response = urllib.urlopen(url)
        data = response.read()
        text = json.loads(data)
        return text
    except Exception:
        return


@app.route('/', methods=['GET', 'POST'])
def index():
    '''Index route'''

    amount = ''
    currency = ''
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form = SelectionForm(from_currency='USD', to_currency='MXN')
    text = query_api()
    if form.validate_on_submit():
        if form.start_amount.data == 0:
            return redirect(url_for('index'))
        if form.to_currency.data == form.from_currency.data:
            amount = form.start_amount.data
            currency = form.to_currency.data
            return render_template('index.html', form=form,
                                   from_rate=form.from_currency.data,
                                   to_rate=form.to_currency.data,
                                   amount=amount, currency=currency,
                                   date_time=date_time)
        if form.from_currency.data == 'USD':
            currency = form.to_currency.data
            amount = form.start_amount.data \
                * text['rates'][form.to_currency.data]
            return render_template('index.html', form=form,
                                   from_rate=form.from_currency.data,
                                   to_rate=form.to_currency.data,
                                   rate=text['rates'][form.to_currency.data],
                                   amount=amount,
                                   date_time=date_time,
                                   currency=currency)
        else:
            currency = form.to_currency.data
            amount = form.start_amount.data \
                / text['rates'][form.from_currency.data]
            return render_template('index.html', form=form,
                                   from_rate=form.from_currency.data,
                                   to_rate=form.to_currency.data,
                                   rate=text['rates'][form.to_currency.data],
                                   date_time=date_time,
                                   amount=amount, currency=currency)
    return render_template('index.html', form=form,
                           from_rate=None,
                           to_rate=None,
                           rate=None,
                           date_time=date_time,
                           amount=None, currency=None)


@app.errorhandler(404)
def page_not_found(error):
    '''404 Page not found'''

    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    '''500 Internal server error'''

    return render_template('500.html'), 500
