import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "dbpython"
)

cursor = conn.cursor()

nome_produto = input ("Insira o nome do produto que deseja deletar:")
comando = f'DELETE FROM vendas WHERE nome_produto = ("{nome_produto}") '
cursor.execute(comando)
conn.commit()
print (f"O produto {nome_produto} foi deletado com sucesso!")

cursor.close()
conn.close()
