from mysql.connector import Error
import mysql.connector
delete from veiculo
where exists(
    SELECT avg(V2.valorDiaria) FROM veiculo v2
    group by v2.marca having avg(v2.valorDiaria) > 300
)
and marca = 'CHEVROLET'


codigo = input('Codigo: ')
placa = input('Placa: ')
marca = input('Marca: ')
modelo = input('Modelo: ')
ano = input('ano: ')
valorDiaria = input('Valor Diaria: ')

dados = codigo + ', ' + placa + ',\'' + marca + '\',\'' + \
    modelo + '\', ' + ano + ', ' + valorDiaria + ')'

declaracao = """INSERT INTO tbl_veiculo
(codigo, placa, marca, modelo, ano, valorDiaria)
VALUES ("""

sql = declaracao + dados
try:
    con = mysql.conectar.coneect(
        host='localhost', database='SIGET', user='julia', password='1234')

    inserir_veiculo = sql
    cursor = con.cursor()
    cursor.execute(inserir_veiculo)
    con.commit()
    print(cursor.rowcount, 'Dados inseridos com sucesso!!')
    cursor.close()
except Error as error:
    print('Falha ao inserir dados {}'.format(error))
