#importando o text
from cgitb import text
from tkinter import*
from tkinter import font 


from tkinter import ttk
from tkinter import messagebox
##importando tkcalendario


#importando a pasta view
from view import*

##
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue
##

janela=Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)


#Dividindo a janela 

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)



frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)




###Cima 

app_nome = Label(frame_cima,text='Lista de dados de Clientes', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place (x=10, y=20) 


#variavel tree global
global tree

#funcao inserir
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    
    #Numeor_de_Matricula = e_Numeor_de Matricula.get()
    lista=[nome, email,telefone]

    if nome=='':
      messagebox.showerror('Erro','0 nome nao pode ser vazio')


    else:
      inserir_info(lista)
      messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso' )

      e_nome.delete(0,'end')
      e_email.delete(0,'end')
      e_telefone.delete(0,'end')


    for Widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()



#funcao atualizar

def atualizar():
    try:
        treev_dados=tree.focus()

        treev_dicionario=tree.item(treev_dados)
        tree_lista=treev_dicionario['values']
 
        valor = tree_lista[0]
        

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        

        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])

    #Botao Atulaizar
        b_confimar = Button(frame_baixo, command=update, text='Confimar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confimar.place(x=105, y=30)
    
   
    except IndexError:
     messagebox.showerror('Erro','Selecionar um dos dos na tabela')
     

#Funcao Delete 
def deletar():
    try:
       treev_dados=tree.focus()

       treev_dicionario=tree.item(treev_dados)
       tree_lista=treev_dicionario['values']
 
       valor = [tree_lista[0]]
       
       
       deletar_info(valor_id)
       messagebox.showinfo('Sucesso','Os dados foram deletados da Tabela com sucesso')





    except IndexError:
       messagebox.showerror('Erro','Selecionar um dos dos na tabela')



 
      









#Nome
l_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10) 
e_nome = Entry(frame_baixo, text='Nome *', width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40) 


#E-MAIL
l_email = Label(frame_baixo,text='Email *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70) 
e_email = Entry(frame_baixo, text='Email *', width=45, justify='left', relief='solid')
e_email.place(x=15, y=100) 


#TELEFONE
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_telefone.place(x=12, y=130) 
e_telefone = Entry(frame_baixo, text='Telefone *', width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160) 




#Botao inserir 

b_inserir = Button(frame_baixo, command=inserir, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co8, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340) 


#Botao Atulaizar
b_Atulaizar = Button(frame_baixo, command=atualizar, text='tualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_Atulaizar.place(x=105, y=340) 


#Botao Delete
b_Delete = Button(frame_baixo, text='Delete', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_Delete.place(x=190, y=340) 





#tabela


def mostrar():
    
    global tree 

    lista = mostrar_info()

    # Cabecario do app 
    tabela_head = ['ID','Nome',  'email','telefone', 'Numero de Matricula']


    # criando a tabela
    tree = ttk.Treeview( selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar( orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(  orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0


    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
    # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)









#teme que chamar a funcão mostar

janela.mainloop()