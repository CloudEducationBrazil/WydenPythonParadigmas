import mysql.connector
from mysql.connector import Error

# tratamento d exceção = erro
try:
    # Parametros de conexao com o BD
    con = mysql.connector.connect(
        host='localhost', database='coursejdbc', user='developer', password='12')

    if (con.is_connected()):
        # Exibir as informacoes do BD
        db_info = con.get_server_info()
        print('conectado', db_info)

        # Exibir o nome BD conectado
        cursor = con.cursor()
        cursor.execute('select database();')
        BD = cursor.fetchone()
        print('Banco de Dados', BD)
    else:
        print('Não conectado!!!', BD)
except Error as e:
    print('Error:', e)
finally:
    # Verifica se o BD está conectado
    if (con.is_connected()):
        cursor.close()
        con.close()
        print('\nConexão encerrada com o MySQL')
