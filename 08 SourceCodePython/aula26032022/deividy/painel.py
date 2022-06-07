import read
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="developer",
    password="12",
    database="dbpython"
)


cursor = conn.cursor()

print('ATENÇÃO --- RESPONDA SOMENTE COM "sim" OU "nao" ')
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print("[ID -- Nome -- Valor]")
print(resultado)


# inserir
inserir = input(">Deseja inserir algum iten na lista?")
if inserir == ('sim'):
    import insert
else:
    print(">>Nenhum produto foi inserido na lista<<")


# update
att = input(">Deseja atualizar algum item da lista?")
if att == ('sim'):
    import update
else:
    print(">>Nenhum item foi atualizado!<<")


# delete
dell = input(">Deseja deletar algum item da lista?")
if dell == ('sim'):
    import delete
else:
    print(">>Nenhum item foi deletado da lista<<")


print("Nova lista atualizada!")


cursor.close()
conn.close()
