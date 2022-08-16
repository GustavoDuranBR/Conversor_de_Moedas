import requests
from datetime import datetime


def texto(msg):
    tam = len(msg)
    print('=' * tam)
    print(f'    {msg}')
    print('=' * tam)


url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL')

data = datetime.now()
data_string = data.strftime('%d/%m/%Y %H:%M')

request = url.json()
cotacao_dolar = request['USDBRL']['bid']
cotacao_euro = request['EURBRL']['bid']
dolar = (float(f'{cotacao_dolar}'))
euro = (float(f'{cotacao_euro}'))

