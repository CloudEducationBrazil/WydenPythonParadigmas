import mysql.connector

conexao = mysql.connector.connect(

    host='localhost',
    user='developer',
    password='12',
    database='app_banco',

)

cursor = conexao.cursor()


Nome_completo = "UILLIAN"
RG = 99323256
CPF = 99986563
CELL = 77742155


#Nome_completo = "HELENO"
#RG = 55555554
#CPF= 44444444
#CELL= 333333333


comando = f'INSERT INTO cadastro (Nome_completo, RG ,CPF,CELL)VALUES("{Nome_completo}", {RG} , {CPF} , {CELL})'
cursor.execute(comando)
conexao.commit()


#comando =  f'SELECT * FROM cadastro'
# cursor.execute(comando)
# resultado=cursor.fetchall() #buscar tudo #ler o banco de dados
# print(resultado)


#CPF = 77777777
# Nome_completo="HELENO"

#comando =  f'UPDATE cadastro SET CPF = {CPF} WHERE Nome_completo = "{Nome_completo}"'
# cursor.execute(comando)
# conexao.commit()


# Nome_completo="UILLIAN"
#comando =  f'DELETE FROM Cadastro WHERE Nome_completo ="{Nome_completo}"'
# cursor.execute(comando)
# conexao.commit()


# cursor.close()
# conexao.close()
