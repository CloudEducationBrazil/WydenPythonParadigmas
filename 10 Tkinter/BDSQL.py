# pip install mysql-connector
import mysql.connector
from mysql.connector import Error

conn = None
# tratamento d exceção = erro
try:
    # Objeto de conexão
    conn = mysql.connector.connect(
        host="localhost", database="coursejdbc", user="developer", password="12")
    if conn.is_connected():
        print("conectado")
        print(conn.get_server_info())

    cursor = conn.cursor()
    cursor.execute("select database(); ")
    linha = cursor.fetchone()
    print("conectado ao banco de dados: ", linha)

    #cursor = conn.cursor()
    nome = "pessoallll"
    sql = f"insert into department (Name) values ('{nome}')"
    cursor.execute(sql)
    conn.commit()
    print("Inserido com sucesso")

    nome = "recursos humanos"
    sql = f"update department set Name = '{nome}' where Id = 63"
    cursor.execute(sql)
    conn.commit()
    print("Atualizado com sucesso")

    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão encerrada")
except Error as e:
    print('Error:', e)
finally:
    # Verifica se o BD está conectado
    if conn != None:
        if (conn.is_connected()):
            cursor.close()
            conn.close()
            print('\nConexão encerrada com o MySQL')
