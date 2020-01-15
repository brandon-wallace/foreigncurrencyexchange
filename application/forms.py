from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired


class SelectionForm(FlaskForm):
    '''Selection fields'''

    start_amount = IntegerField('START AMOUNT:', validators=[InputRequired()])
    from_currency = SelectField('FROM:', choices=[
                               ('USD', 'US Dollar (USD)'),
                               ('AUD', 'Australian Dollar (AUD)'),
                               ('BGN', 'Bulgarian Lev (BGN)'),
                               ('BRL', 'Brazilian Real (BRL)'),
                               ('CAD', 'Canadian dollar (CAD)'),
                               ('CHF', 'Swiss Franc (CHF)'),
                               ('CNY', 'Chinese Yuan (CNY)'),
                               ('CZK', 'Czech Koruna (CZK)'),
                               ('DKK', 'Danish Krone (DKK)'),
                               ('EUR', 'Euro (EUR)'),
                               ('GBP', 'British Pound (GBP)'),
                               ('HKD', 'Hong Kong Dollar (HKD)'),
                               ('HRK', 'Croatian Kuna (HRK)'),
                               ('HUF', 'Hungarian Forint (HUF)'),
                               ('IDR', 'Indonesian Rupiah (IDR)'),
                               ('ILS', 'Israeli Shekel (ILS)'),
                               ('INR', 'Indian Rupee (INR)'),
                               ('ISK', 'Icelandic Krona (ISK)'),
                               ('JPY', 'Japanese Yen (JPY)'),
                               ('KRW', 'South Korean Won (KRW)'),
                               ('MYR', 'Malaysian Ringgit (MYR)'),
                               ('MXN', 'Mexican Peso (MXN)'),
                               ('NOK', 'Norwegian Krone (NOK)'),
                               ('NZD', 'New Zealand (NZD)'),
                               ('PHP', 'Philippine Peso (PHP)'),
                               ('PLN', 'Polish Zloty (PLN)'),
                               ('RON', 'Romanian Leu (RON)'),
                               ('RUB', 'Russian Ruble (RUB)'),
                               ('SEK', 'Swedish Krona (SEK)'),
                               ('SGD', 'Singapore Dollar (SGD)'),
                               ('THB', 'Thai Baht (THB)'),
                               ('TRY', 'Turkish Lira (TRY)'),
                               ('ZAR', 'South African Rand (ZAR)')
                               ])
    to_currency = SelectField('TO:', choices=[
                               ('AUD', 'Australian Dollar (AUD)'),
                               ('BGN', 'Bulgarian Lev (BGN)'),
                               ('BRL', 'Brazilian Real (BRL)'),
                               ('CAD', 'Canadian dollar (CAD)'),
                               ('CHF', 'Swiss Franc (CHF)'),
                               ('CNY', 'Chinese Yuan (CNY)'),
                               ('CZK', 'Czech Koruna (CZK)'),
                               ('DKK', 'Danish Krone (DKK)'),
                               ('EUR', 'Euro (EUR)'),
                               ('GBP', 'British Pound (GBP)'),
                               ('HKD', 'Hong Kong Dollar (HKD)'),
                               ('HRK', 'Croatian Kuna (HRK)'),
                               ('HUF', 'Hungarian Forint (HUF)'),
                               ('IDR', 'Indonesian Rupiah (IDR)'),
                               ('ILS', 'Israeli Shekel (ILS)'),
                               ('INR', 'Indian Rupee (INR)'),
                               ('ISK', 'Icelandic Krona (ISK)'),
                               ('JPY', 'Japanese Yen (JPY)'),
                               ('KRW', 'South Korean Won (KRW)'),
                               ('MYR', 'Malaysian Ringgit (MYR)'),
                               ('MXN', 'Mexican Peso (MXN)'),
                               ('NOK', 'Norwegian Krone (NOK)'),
                               ('NZD', 'New Zealand (NZD)'),
                               ('PHP', 'Philippine Peso (PHP)'),
                               ('PLN', 'Polish Zloty (PLN)'),
                               ('RON', 'Romanian Leu (RON)'),
                               ('RUB', 'Russian Ruble (RUB)'),
                               ('SEK', 'Swedish Krona (SEK)'),
                               ('SGD', 'Singapore Dollar (SGD)'),
                               ('THB', 'Thai Baht (THB)'),
                               ('TRY', 'Turkish Lira (TRY)'),
                               ('USD', 'US Dollar (USD)'),
                               ('ZAR', 'South African Rand (ZAR)')
                               ])
    submit = SubmitField('CALCULATE')
