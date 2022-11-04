# https: // docs.python.org/pt-br/dev/library/tkinter.html

# Interface Gráfica:
# Passos: 1. Importar a bib tkinter; 2. Criar uma função; 3. Criar a janela utilizando o tkinter
# 4. Invocar uma função

from pip._vendor import requests
from tkinter import *
#from tkinter import ttk

import os


def semComando():
    pass


app = Tk()
app.title('Sistema Acadêmico Yduqs')
app.geometry("500x330")  # largura x altura
app.configure(bg='#dde')

barraDeMenu = Menu(app)
menuCadastros = Menu(barraDeMenu, tearoff=0)
menuCadastros.add_command(label="Alunos", command=semComando)
menuCadastros.add_command(label="Professores", command=semComando)
menuCadastros.add_command(label="Disciplinas", command=semComando)
menuCadastros.add_separator()
menuCadastros.add_command(label="Fechar", command=app.quit)

menuTabelas = Menu(barraDeMenu, tearoff=0)
menuTabelas.add_command(label="Estados", command=semComando)
menuTabelas.add_command(label="Feriados", command=semComando)

menuSobre = Menu(barraDeMenu, tearoff=0)
menuSobre.add_command(label="Sobre", command=semComando)

barraDeMenu.add_cascade(label="Cadastros", menu=menuCadastros)
barraDeMenu.add_cascade(label="Tabelas", menu=menuTabelas)
barraDeMenu.add_cascade(label="Sobre")

app.config(menu=barraDeMenu)

#listEsportes = ["Futebol", "Basquete"]
#lbEsportes = Label(app, text="Esportes")
# lbEsportes.pack()

#cb_esportes = ttk.Combobox(app, values=listEsportes)
# cb_esportes.set("Futebol")
# cb_esportes.pack()

app.mainloop()
