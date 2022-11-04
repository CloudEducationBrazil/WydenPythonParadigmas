import mysql.connector
from mysql.connector import Error

con = None
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

        # Consulta no BD - Read
        consulta_sql = 'select Id, Name from department where Id = 55'
        #cursor = con.cursor()
        cursor.execute(consulta_sql)

        # Captura os registros da Table do BD
        linhas = cursor.fetchall()

        # Total de Regs do Table
        print()
        print('Total registros:', cursor.rowcount)
        print()

        # Exibir os registros da Table
        print('***** Registros *******')
        for linha in linhas:
            print(f'Id:{linha[0]} Name:{linha[1]}')
            #print('Id:%d Name:%s' % (linha[0], linha[1]))
            #print('Name:', linha[1])
    else:
        print('Não conectado!!!', BD)
except Error as e:
    print('Error:', e)
finally:
    # Verifica se o BD está conectado
    if con != None:
        if (con.is_connected()):
            cursor.close()
            con.close()
            print('\nConexão encerrada com o MySQL')
