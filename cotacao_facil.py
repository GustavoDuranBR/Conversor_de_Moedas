import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb  # Pacote para um visual mais moderno
import requests
from datetime import datetime

# Função para buscar cotações
def pegar_cotacao():
    url = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,GBP-BRL,ARS-BRL,JPY-BRL')
    request = url.json()

    cotacao_dolar = float(request['USDBRL']['bid'])
    cotacao_euro = float(request['EURBRL']['bid'])
    cotacao_libra = float(request['GBPBRL']['bid'])
    cotacao_peso = float(request['ARSBRL']['bid'])
    cotacao_iene = float(request['JPYBRL']['bid'])

    texto = f"""
    💵 Dólar: U$ {cotacao_dolar:.2f}
    💶 Euro: €$ {cotacao_euro:.2f}
    💷 Libra: £$ {cotacao_libra:.2f}
    🇦🇷 Peso Argentino: $ {cotacao_peso:.2f}
    🇯🇵 Iene Japonês: ¥ {cotacao_iene:.2f}
    """
    
    label_cotacoes.config(text=texto)

# Criando janela principal
janela = tb.Window(themename="darkly")  
janela.title("Cotação Fácil – Prático e acessível")
janela.geometry("400x350")  

# Substituindo o ícone do Tkinter
janela.iconbitmap("icone_moeda.ico")  

# Cabeçalho
frame_topo = ttk.Frame(janela)
frame_topo.pack(pady=10)

label_titulo = ttk.Label(frame_topo, text="💰 Cotação Fácil", font=("Arial", 16, "bold"))
label_titulo.pack()

data_string = datetime.now().strftime('%d/%m/%Y %H:%M')
label_data = ttk.Label(frame_topo, text=f"Atualizado em: {data_string}", font=("Arial", 10))
label_data.pack()

# Botão estilizado
botao_cotacao = ttk.Button(janela, text="🔄 Atualizar Cotações", bootstyle="success", command=pegar_cotacao)
botao_cotacao.pack(pady=15)

# Área de exibição das cotações
label_cotacoes = ttk.Label(janela, text="", font=("Arial", 12), justify="left")
label_cotacoes.pack(pady=10)

# Rodapé
label_rodape = ttk.Label(janela, text="Desenvolvido por Gustavo Duran", font=("Arial", 8))
label_rodape.pack(side="bottom", pady=5)

janela.mainloop()
