from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired


class SelectionForm(FlaskForm):
    '''Selection fields'''

    start_amount = IntegerField('START AMOUNT:', validators=[InputRequired()])
    from_currency = SelectField('FROM:', choices=[
                               ('CAD', 'Canadian dollar (CAD)'),
                               ('HKD', 'Hong Kong Dollar (HKD)'),
                               ('ISK', 'Icelandic Krona (ISK)'),
                               ('PHP', 'Philippine Peso (PHP)'),
                               ('DKK', 'Danish Krone (DKK)'),
                               ('HUF', 'Hungarian Forint (HUF)'),
                               ('CZK', 'Czech Koruna (CZK)'),
                               ('GBP', 'British Pound (GBP)'),
                               ('RON', 'Romanian Leu (RON)'),
                               ('SEK', 'Swedish Krona (SEK)'),
                               ('IDR', 'Indonesian Rupiah (IDR)'),
                               ('INR', 'Indian Rupee (INR)'),
                               ('BRL', 'Brazilian Real (BRL)'),
                               ('RUB', 'Russian Ruble (RUB)'),
                               ('HRK', 'Croatian Kuna (HRK)'),
                               ('JPY', 'Japanese Yen (JPY)'),
                               ('THB', 'Thai Baht (THB)'),
                               ('CHF', 'Swiss Franc (CHF)'),
                               ('EUR', 'Euro (EUR)'),
                               ('MYR', 'Malaysian Ringgit (MYR)'),
                               ('BGN', 'Bulgarian Lev (BGN)'),
                               ('TRY', 'Turkish Lira (TRY)'),
                               ('CNY', 'Chinese Yuan (CNY)'),
                               ('NOK', 'Norwegian Krone (NOK)'),
                               ('NZD', 'New Zealand (NZD)'),
                               ('ZAR', 'South African Rand (ZAR)'),
                               ('USD', 'US Dollar (USD)'),
                               ('MXN', 'Mexican Peso (MXN)'),
                               ('SGD', 'Singapore Dollar (SGD)'),
                               ('AUD', 'Australian Dollar (AUD)'),
                               ('ILS', 'Israeli Shekel (ILS)'),
                               ('KRW', 'South Korean Won (KRW)'),
                               ('PLN', 'Polish Zloty (PLN)')
                               ])
    to_currency = SelectField('TO:', choices=[
                               ('CAD', 'Canadian dollar (CAD)'),
                               ('HKD', 'Hong Kong Dollar (HKD)'),
                               ('ISK', 'Icelandic Krona (ISK)'),
                               ('PHP', 'Philippine Peso (PHP)'),
                               ('DKK', 'Danish Krone (DKK)'),
                               ('HUF', 'Hungarian Forint (HUF)'),
                               ('CZK', 'Czech Koruna (CZK)'),
                               ('GBP', 'British Pound (GBP)'),
                               ('RON', 'Romanian Leu (RON)'),
                               ('SEK', 'Swedish Krona (SEK)'),
                               ('IDR', 'Indonesian Rupiah (IDR)'),
                               ('INR', 'Indian Rupee (INR)'),
                               ('BRL', 'Brazilian Real (BRL)'),
                               ('RUB', 'Russian Ruble (RUB)'),
                               ('HRK', 'Croatian Kuna (HRK)'),
                               ('JPY', 'Japanese Yen (JPY)'),
                               ('THB', 'Thai Baht (THB)'),
                               ('CHF', 'Swiss Franc (CHF)'),
                               ('EUR', 'Euro (EUR)'),
                               ('MYR', 'Malaysian Ringgit (MYR)'),
                               ('BGN', 'Bulgarian Lev (BGN)'),
                               ('TRY', 'Turkish Lira (TRY)'),
                               ('CNY', 'Chinese Yuan (CNY)'),
                               ('NOK', 'Norwegian Krone (NOK)'),
                               ('NZD', 'New Zealand (NZD)'),
                               ('ZAR', 'South African Rand (ZAR)'),
                               ('USD', 'US Dollar (USD)'),
                               ('MXN', 'Mexican Peso (MXN)'),
                               ('SGD', 'Singapore Dollar (SGD)'),
                               ('AUD', 'Australian Dollar (AUD)'),
                               ('ILS', 'Israeli Shekel (ILS)'),
                               ('KRW', 'South Korean Won (KRW)'),
                               ('PLN', 'Polish Zloty (PLN)')
                               ])
    submit = SubmitField('CALCULATE')
