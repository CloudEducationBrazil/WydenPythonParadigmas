# tkinter é um conjunto de envólucros que implementam os widgets Tk como classes Python.
# As principais virtudes do tkinter são que ele é rápido, e que geralmente vem junto
# com o Python.
# Embora sua documentação padrão seja fraca, um bom material está disponível,
# que inclui: referências, tutoriais, um livro e outros.

# https: // docs.python.org/pt-br/dev/library/tkinter.html

# interface gráfica (GUI) e interface de comandos CLI)
# k é um kit de ferramentas de interface gráfica do usuário que leva o desenvolvimento de aplicativos de desktop
#  a um nível mais alto do que as abordagens convencionais.

# import requests
# python.exe -m pip install --upgrade pip
# python -m venv venv
# pip install requests;
# pip install lxml

# interfaces Gráficas: pandas; PyCharm; Bryton; kivy; DJango; Flask, etc
# Transformar em EXE (Distribuição): pip install pyinstaller
# pyinstaller --onefile arquivo.py

# Interface Gráfica:
# Passos: 1. Importar a bib tkinter; 2. Criar uma função; 3. Criar a janela utilizando o tkinter
# 4. Invocar uma função

# import pip._vendor.requests as requests
from pip._vendor import requests
from tkinter import *


def pegar_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    requisicao = requests.get(url)
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_bitcoin = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    Bitcoin: {cotacao_bitcoin}
    '''
    # print(texto)
    app.geometry("330x200")
    exibe_cotacoes['text'] = texto


# Tk()
# pegar_cotacoes()
app = Tk()
app.title('Cotação de Moedas: USD, EUR, BTC')
app.geometry("330x100")  # largura x altura
app.configure(bg='#dde')

# primeiro criar o texto, depois associar ao grid para posicionar
# anchor =N ; S; E = Leste W= Oeste; NE;SE;SO;NO
header_tela = Label(
    app, text='Clique no botão para visualizar as cotações de moedas ...').grid(column=0, row=0, padx=10, pady=10)

botao = Button(app, text="Buscar cotacões USD, EUR, BTC",
               command=pegar_cotacoes).grid(column=0, row=1, padx=10, pady=10)

exibe_cotacoes = Label(
    app, text='')  # .grid(column=0, row=2, padx=10, pady=10)

#header_tela.grid(column=0, row=0, padx=10, pady=10)
#botao.grid(column=0, row=1, padx=10, pady=10)
exibe_cotacoes.grid(column=0, row=2, padx=10, pady=10)

app.mainloop()
