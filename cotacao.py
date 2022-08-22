import PySimpleGUI as sg
from conversor import *


class TelaPrincipal:
    def __init__(self):
        sg.theme('Dark Grey 15')
        layout = [
            [sg.Text('Cotação de Moedas')],
            [sg.Text('Valor desejado: R$'), sg.InputText(size=(15, 0), key='valor')],
            [sg.Text(f'U$ {dolar:.3}')],
            [sg.Text(f'€$ {euro:.3}')],
            [sg.Text(f'₿$ {btc_brl}')],
            [sg.Text(f'₿$ {btc_usd}')],
            [sg.Button('Converter'), sg.Button('Cancelar')],
            [sg.Output(size=(45, 15))],
            [sg.Text('Developed by Gustavo Duran')],
            [sg.Text('https://github.com/GustavoDuranBR')]
        ]

        janela = sg.Window('Conversor de Moedas', layout)

        while True:
            self.evento, self.valores = janela.read()
            if self.evento == sg.WIN_CLOSED or self.evento == 'Cancelar':
                break
            if self.evento == 'Converter':
                texto_entrada = self.valores['valor']
                entrada_str = str(texto_entrada).replace(',', '.')
                valor = float(entrada_str)
                conv_dolar = valor / dolar
                conv_euro = valor / euro
                conv_btc_br = valor / btc_brl
                conv_btc_us = valor / btc_usd
                texto(data_string)
                brl = f'{valor:.2f}'
                usd = f'{conv_dolar:.2f}'
                eur = f'{conv_euro:.2f}'
                btc_br = f'{conv_btc_br:.6f}'
                btc_us = f'{conv_btc_us:.6f}'
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

        janela.close()

    def iniciar(self):
        print(self.valores)


tela = TelaPrincipal()
tela.iniciar()
