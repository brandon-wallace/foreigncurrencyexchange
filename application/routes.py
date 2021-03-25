# application/routes.py
from pprint import pprint
import json
import urllib.request
from os import environ
from datetime import datetime, date, timedelta
from flask import render_template, url_for, redirect
from application import app
from application.forms import SelectionForm

api_key = environ.get('API_KEY')

today = date.today()
todays_date = today + timedelta(days=1)
rate_30_days_ago = today - timedelta(days=30)
rate_60_days_ago = today - timedelta(days=60)
rate_60_days = today - timedelta(days=59)

print(api_key)
print(today)
print(todays_date)
print(rate_30_days_ago)
print(rate_60_days_ago)


def query_api(base, end):
    '''Query API for exchange rates'''

    try:
        #url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
        url = f'https://api.exchangeratesapi.io/history?start_at={rate_60_days_ago}&end_at={todays_date}&base=USD&symbols={base},{end}'
        response = urllib.request.urlopen(url)
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
    if form.validate_on_submit():
        text = query_api(form.from_currency.data, form.to_currency.data)
        print(text)
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
                * text['rates'][today.strftime('%Y-%m-%d')][form.to_currency.data]
            thirty_days_ago = form.start_amount.data \
                * text['rates'][rate_30_days_ago.strftime('%Y-%m-%d')][form.to_currency.data]
            sixty_days_ago = form.start_amount.data \
                * text['rates'][rate_60_days.strftime('%Y-%m-%d')][form.to_currency.data]
            print(thirty_days_ago)
            print(sixty_days_ago)
            return render_template('index.html', form=form,
                                   from_rate=form.from_currency.data,
                                   to_rate=form.to_currency.data,
                                   rate="99.99",# text['conversion_rates'][form.to_currency.data],
                                   amount=amount,
                                   date_time=date_time,
                                   currency=currency)
        # else:
        #     currency = form.to_currency.data
        #     amount = form.start_amount.data \
        #         / text['conversion_rates'][form.from_currency.data]
        #     return render_template('index.html', form=form,
        #                            from_rate=form.from_currency.data,
        #                            to_rate=form.to_currency.data,
        #                            rate=text['conversion_rates'][form.to_currency.data],
        #                            date_time=date_time,
        #                            amount=amount, currency=currency)
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
