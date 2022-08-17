import requests
from datetime import datetime


def texto(msg):
    tam = len(msg)
    print('=' * tam)
    print(f'    {msg}')
    print('=' * tam)


url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,BTC-USD')

data = datetime.now()
data_string = data.strftime('%d/%m/%Y %H:%M')

request = url.json()
cotacao_dolar = request['USDBRL']['bid']
cotacao_euro = request['EURBRL']['bid']
real_bitcoin = request['BTCBRL']['bid']
dolar_bitcoin = request['BTCUSD']['bid']
dolar = (float(f'{cotacao_dolar}'))
euro = (float(f'{cotacao_euro}'))
btc_brl = (float(f'{real_bitcoin}'))
btc_usd = (float(f'{dolar_bitcoin}'))

