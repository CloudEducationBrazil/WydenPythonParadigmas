# https: // docs.python.org/pt-br/dev/library/tkinter.html

# Interface Gráfica:
# Passos: 1. Importar a bib tkinter; 2. Criar uma função; 3. Criar a janela utilizando o tkinter
# 4. Invocar uma função

from pip._vendor import requests
from tkinter import *
import os
import bancoAlunos


def listar():
    os.system('cls')
    print('Nome:%s' % vNome.get())
    print('Telefone:%s' % vTelefone.get())
    print('E-mail:%s' % vEmail.get())
    print('Obs:%s' % vObs.get("1.0", END))


def gerarTXT():
    pastaApp = os.path.dirname(__file__)
    # print(pastaApp)
    nomarqAlu = pastaApp+"\\aluno.txt"
    arqAlu = open(nomarqAlu, 'a')
    arqAlu.write('Nome:%s' % vNome.get())
    arqAlu.write('\nTelefone:%s' % vTelefone.get())
    arqAlu.write('\nE-mail:%s' % vEmail.get())
    arqAlu.write('\nObs:%s' % vObs.get("1.0", END))
    arqAlu.write('\n')
    arqAlu.close()


def inserirAluno():
    if vNome.get() != "":
        vnome = vNome.get()
        vtelefone = vTelefone.get()
        vobs = vObs.get("1.0", END)
        vquery = "INSERT INTO tb_aluno (NOME, TEL, EMAIL, OBS) VALUES ('" + \
            vnome+"', '"+vtelefone+"', '"+vemail+"', '"+vobs+"' )"
        bancdoAlunos.dml(vquery)

        # Limpando os campos
        vNome.delete(0, END)
        vTelefone.delete(0, END)
        vEmail.delete(0, END)
        vObs.delete("1.0", END)

        print('Dados gravados com sucesso ...')
    else:
        print('Erro na inclusão dos dados!!!')


app = Tk()
app.title('Cadastro de Alunos')
app.geometry("500x330")  # largura x altura
app.configure(bg='#dde')

# primeiro criar o texto, depois associar ao grid para posicionar
# anchor =N ; S; E = Leste W= Oeste; NE;SE;SO;NO
Label(
    app, text='Nome',
    bg='#dde', fg='#009', anchor=W).place(x=10, y=10, width=100, height=20)

# Input
vNome = Entry(app)
vNome.place(x=10, y=30, width=200, height=20)

Label(
    app, text='Telefone',
    bg='#dde', fg='#009', anchor=W).place(x=10, y=60, width=100, height=20)

# Input
vTelefone = Entry(app)
vTelefone.place(x=10, y=80, width=100, height=20)

Label(
    app, text='Email',
    bg='#dde', fg='#009', anchor=W).place(x=10, y=110, width=100, height=20)

# Input
vEmail = Entry(app)
vEmail.place(x=10, y=140, width=300, height=20)

Label(
    app, text='Obs',
    bg='#dde', fg='#009', anchor=W).place(x=10, y=170, width=100, height=20)

# Input
vObs = Text(app)
vObs.place(x=10, y=190, width=300, height=80)

Button(app, text="Imprimir",
       command=listar).place(x=10, y=290, width=100, height=20)

Button(app, text="Gerar TXT",
       command=gerarTXT).place(x=120, y=290, width=100, height=20)

app.mainloop()
