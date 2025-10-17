import mysql.connector
import os

def menu():
    os.system('cls')

    print("CRUD User: ") 
    print("1 Exibir BD: ") 
    print("2 Listar: ") 
    print("3 Incluir: ") 
    print("4 Alterar: ") 
    print("5 Excluir: ") 
    
def mostrarDB():
    cursor.execute("select database(); ")
    linha = cursor.fetchone()
    print("conectado ao banco de dados: ", linha)
    
def fecharConexao():
    if conn.is_connected(): # testando se está conectado
        cursor.close()
        conn.close()
        print("Conexão encerrada")

def listarUsers():
    sql = "select * from user"
    cursor.execute(sql)
    linha = cursor.fetchall()
    print(linha)
    
def incluirUser():
    nome  = input("Informe o nome: ")
    idade = int(input("Informe idade: "))
    
    sql = "insert into user (nome, idade) values (%s, %s)"
    valores = (nome, idade)

    cursor.execute(sql, valores)
    conn.commit()
    print("Inserido com sucesso")

def alterarUser():
    id  = int(input("Informe o Id: "))

    sql = "select * from user where id = %s"
    valor = (id,)

    cursor.execute(sql, valor)
    
    if cursor.rowcount > 0:
        print(f"\nUsuário encontrado: ID={linha[0]}, Nome={linha[1]}, Idade={linha[2]}")
        
        print("Para manter o dado pressione <ENTER>")
        nome_input  = input("Informe o nome: ")
        idade_input = input("Informe idade: ")
        
        # Mantém os valores antigos se o usuário não digitar nada
        nome = nome_input if nome_input.strip() != "" else linha[1]
        idade = int(idade_input) if idade_input.strip() != "" else linha[2]    

        sql = "update user set nome = %s, idade = %s where id = %s"
        valores = (nome, idade, id)

        cursor.execute(sql, valores)
        conn.commit() 
        print("Alterado com sucesso")
    else: 
        print("User não encontrado")

def excluirUser():
    try:
        id = int(input("Informe o Id: "))

        # Verifica se o ID existe antes de excluir
        cursor.execute("SELECT nome, idade FROM user WHERE id = %s", (id,))
        usuario = cursor.fetchone()

        if usuario is None:
            print("Código não encontrado.")
            return
        
        print(f"\nUsuário encontrado: {usuario[0]} ({usuario[1]} anos)")
        confirmar = input("Deseja realmente excluir este usuário? (S/N): ").strip().upper()

        if confirmar != "S":
            print("Exclusão cancelada pelo usuário.")
            return

        # Executa a exclusão
        cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        conn.commit()

        print("Usuário excluído com sucesso!")

    except ValueError:
        print("ID inválido. Informe um número inteiro.")
    except Exception as e:
        conn.rollback()  # reverte qualquer alteração se der erro
        print(f"Erro ao excluir usuário: {e}")

# Objeto de conexão
conn = mysql.connector.connect(
    host="localhost", database="agendadb", user="root", password="123456")
if conn.is_connected():
    print("conectado") # print(conn.get_server_info()) (versão)

    cursor = conn.cursor()

    op = ""
    while op != "0":
        menu()
        op = input("Opção: ") 
    
        match op:
            case "1": 
                mostrarDB()
            case "2": 
                listarUsers()
            case "3":
                incluirUser()
            case "4":
                alterarUser()
            case "5":
                excluirUser()
            case _: 
                print("Opção Inválida")
                
        input("Pressione Enter para continuar...")