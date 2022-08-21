from tkinter import *
import requests
from datetime import datetime


data = datetime.now()
data_string = data.strftime('%d/%m/%Y %H:%M')


def texto_formatado():
    texto_orientacao = Label(janela, text=f'{"*" * 36}')
    texto_orientacao1 = Label(janela, text='    Cotação de Moedas   ')
    texto_data_hora1 = Label(janela, text=f'{data_string}')
    texto_data_hora2 = Label(janela, text=f'{"*" * 36}')

    texto_orientacao.grid(column=0, row=0, padx=10, pady=2)
    texto_orientacao1.grid(column=0, row=1, padx=10, pady=2)
    texto_data_hora1.grid(column=0, row=3, padx=10, pady=2)
    texto_data_hora2.grid(column=0, row=4, padx=10, pady=2)


def botao():
    botao1 = Button(janela, text='Pegar Cotação', command=pegar_cotacao)
    botao1.grid(column=0, row=5, padx=10, pady=2)


def pegar_cotacao():
    url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-USD,BTC-BRL')
    request = url.json()
    cotacao_dolar = request['USDBRL']['bid']
    cotacao_euro = request['EURBRL']['bid']
    real_bitcoin = request['BTCBRL']['bid']
    dolar_bitcoin = request['BTCUSD']['bid']
    dolar = (float(f'{cotacao_dolar}'))
    euro = (float(f'{cotacao_euro}'))
    btc_brl = (float(f'{real_bitcoin}'))
    btc_usd = (float(f'{dolar_bitcoin}'))

    texto = f'''
    Dólar........U$ {dolar:.2f}
    Euro.........€$ {euro:.2f}
    ₿itcoin......R$ {btc_brl:.3f} 
    ₿itcoin......U$ {btc_usd:.3f}
    '''
    texto_saida['text'] = texto


janela = Tk()

texto_formatado()
botao()
texto_saida = Label(janela, text="")
texto_saida.grid(column=0, row=7, padx=10, pady=2)

janela.mainloop()
