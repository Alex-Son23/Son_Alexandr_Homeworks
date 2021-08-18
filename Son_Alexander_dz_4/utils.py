import requests
import datetime


def currency_rates(currency):
    currency = ''.join(currency[1:])
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currencies = str(response.content)
    number_currency = currencies.find(currency.upper())
    val = '<Value>'
    if number_currency > 0:
        start_value = currencies[number_currency:].find(val) + number_currency + len(val)
        end_value = currencies[start_value:].find('<') + start_value
        value = currencies[start_value:end_value]
        date = str(currencies[currencies.find('Date=')+6:currencies.find('name') - 2]).split('.')
        for index, elem in enumerate(date):
            date[index] = int(elem)
        right_date = datetime.datetime(year=date[2], month=date[1], day=date[0])
        print(right_date.date())
        print(value)
        return f'{value}'
    else:
        print(None)
        return 'None'