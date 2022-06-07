import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="developer",
    password="12",
    database="dbpython"
)

cursor = conn.cursor()

nome_produto = input("Insira o nome do produto:")
nome_cliente = input("Insira o nome do cliente:")
print("***Lembre-se de não utilizar virgulas para definir o valor, e sim um ponto!***")
valor = input("Insira o valor do produto:")
data_compra = input("Insira a data da compra no modelo DD/MM/AAAA:")
comando = f'INSERT INTO vendas (nome_produto, valor, nome_cliente, data_compra) VALUES ("{nome_produto}", {valor}, "{nome_cliente}", "{data_compra}") '
cursor.execute(comando)
conn.commit()
print(f"A compra do cliente {nome_cliente} foi inserida com sucesso!")

cursor.close()
conn.close()
