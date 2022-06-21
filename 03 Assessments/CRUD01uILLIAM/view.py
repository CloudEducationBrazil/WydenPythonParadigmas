# importando sqlite
import sqlite3 as lite

# criando conexao
con = lite.connect("dados.db")




# Inserindo informacoes 
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone) VALUES (?,?,?)"
        cur.execute(query,i)




#Acessar informacoes 
def mostrar_info():
    lista=[]
    with con:
        cur = con.cursor()
        query="SELECT * FROM formulario"
        cur.execute(query)
        informacao=cur.fetchall()
        
        for i in informacao:
            lista.append(i)

    return lista



 
#Atualizar informacoes 
def atuliazar_infor(i):

    with con:
     cur = con.cursor()
     query = "UPDATE formulario SET nome=? email=? telefone=? WHERE id=?"
     cur.execute(query,i)


#Delet
def deletar(i):
  with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query,i)
