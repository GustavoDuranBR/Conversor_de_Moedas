import PySimpleGUI as sg
from conversor import *
from conversor import leia_float


class Tela:

    sg.theme('Dark Grey 15')

    def __init__(self):
        layout = [
            [sg.Text('Cotação de Moedas')],
            [sg.Text('Valor desejado: R$'), sg.Input(size=(15, 0), key='texto')],
            [sg.Text(f'U$ {dolar:.3f}')],
            [sg.Text(f'€$ {euro:.3f}')],
            [sg.Text(f'₿$ {btc_brl}')],
            [sg.Text(f'₿$ {btc_usd}')],
            [sg.Button('Converter'), sg.Button('Cancelar')],
            [sg.Output(size=(45, 15))]
        ]
        self.janela = sg.Window('Conversor de Moedas', layout)

        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED or evento == 'Cancelar':
                break
            if evento == 'Converter':
                texto_entrada = valores['texto']
                valor = float(texto_entrada)
                conv_dolar = valor / dolar
                conv_euro = valor / euro
                conv_btc_br = valor / btc_brl
                conv_btc_us = valor / btc_usd
                texto(data_string)
                brl = (round(valor, 2))
                usd = (round(conv_dolar, 2))
                eur = (round(conv_euro, 2))
                btc_br = (round(conv_btc_br, 8))
                btc_us = (round(conv_btc_us, 8))
                brl_texto = str(brl).replace('.', ',')
                usd_texto = str(usd).replace('.', ',')
                eur_texto = str(eur).replace('.', ',')
                btc_br_texto = str(btc_br).replace('.', ',')
                btc_us_texto = str(btc_us).replace('.', ',')
                print(f'R$ {brl_texto}')
                print(f'U$ {usd_texto}')
                print(f'€$ {eur_texto}')
                print(f'₿-R$ {btc_br_texto}')
                print(f'₿-U$ {btc_us_texto}')

        self.janela.close()


janela = Tela()
