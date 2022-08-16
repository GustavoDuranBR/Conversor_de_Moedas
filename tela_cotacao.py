import PySimpleGUI as sg
from conversor import *

layout = [
    [sg.Text('Cotação de Moedas')],
    [sg.Text('Valor desejado: R$'), sg.Input(size=(15, 0), key='texto')],
    [sg.Text('Dólar'), sg.Text(f'USD U$ {dolar:.3}')],
    [sg.Text('Euro '), sg.Text(f'EUR €$ {euro:.3}')],
    [sg.Button('Converter'), sg.Button('Cancelar')],
    [sg.Output(size=(45, 15))]
]

janela = sg.Window('Conversor de Moedas', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Converter':
        texto_entrada = valores['texto']
        valor = float(texto_entrada)
        conv_dolar = valor / dolar
        conv_euro = valor / euro
        texto(data_string)
        brl = (round(valor, 2))
        usd = (round(conv_dolar, 2))
        eur = (round(conv_euro, 2))
        brl_texto = str(brl).replace('.', ',')
        usd_texto = str(usd).replace('.', ',')
        eur_texto = str(eur).replace('.', ',')
        print(f'BRL {brl_texto}')
        print(f'USD {usd_texto}')
        print(f'EUR {eur_texto}')

janela.close()
