import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="developer", password="12", database="coursejdbc")

cursor = conexao.cursor()

if conexao.is_connected():
    print("conectado")
else:
    print('erro')

comando = f'delete from veiculo where marca = "CHEVROLET" and exists(SELECT avg(v2.valorDiaria) FROM veiculo v2 group by v2.marca having avg(v2.valorDiaria) > 300 )'

# /*
# delete from veiculo
# where exists(select tab.valorDiaria from
#             (SELECT v2.valorDiaria
# FROM veiculo v2
#              where v2.marca='CHEVROLET'
#              group by v2.marca
#              having avg(v2.valorDiaria) > 300) as tab)
# and marca = "CHEVROLET"
# */

cursor.execute(comando)
conexao.commit()
print('dados excluídos com sucesso!!!')

cursor.close()
conexao.close()
